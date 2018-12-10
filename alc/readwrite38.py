from ctypes import *
import numpy as np
import sys, struct

##################################################################
##################################################################
##################################################################
def read_record( ifs ):
    lenrec_s_bin  = ifs.read( 4 )
    lenrec_s      = (struct.unpack( 'i', lenrec_s_bin ))[0]
    #print( "read: s: %10d" % ( lenrec_s ) )
    data = ifs.read( lenrec_s )
    lenrec_e_bin  = ifs.read( 4 )
    lenrec_e      = (struct.unpack( 'i', lenrec_e_bin ))[0]
    #print( "read: e: %10d" % ( lenrec_e ) )
    return data

def write_record( ofs, data, nbyte ):
    ofs.write( struct.pack( 'i', nbyte) )
    ofs.write( data )
    ofs.write( struct.pack( 'i', nbyte) )


##################################################################
##################################################################
##################################################################
def read_record( ifs ):
    lenrec_s_bin  = ifs.read( 4 )
    lenrec_s      = (struct.unpack( 'i', lenrec_s_bin ))[0]
    #print( "read: s: %10d" % ( lenrec_s ) )
    data = ifs.read( lenrec_s )
    lenrec_e_bin  = ifs.read( 4 )
    lenrec_e      = (struct.unpack( 'i', lenrec_e_bin ))[0]
    #print( "read: e: %10d" % ( lenrec_e ) )
    return data

def write_record( ofs, data, nbyte ):
    ofs.write( struct.pack( 'i', nbyte) )
    ofs.write( data )
    ofs.write( struct.pack( 'i', nbyte) )

#################################
#################################
#################################
def read38( fname ):
    irecord = 1
    
    ifs   = open( fname, 'rb' )
    nso = np.empty( [ 20 ], dtype = np.int32 )
    nmo = np.empty( [ 20 ], dtype = np.int32 )
    
    ###
    ### Skip Unnecessary Records
    ###
    for irec in range( 1, irecord ):
        data  = read_record( ifs )
        name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
        nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
        nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
        nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
        nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
        for i in range( nsym ):
            if ( nso[ i ]*nmo[ i ] == 0 ):
                continue
            data  = read_record( ifs )
        nsym = 0
    
    ###
    ### Read Required Records
    ###
    ### Basic Data
    data  = read_record( ifs )
    name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
    nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
    nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
    nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
    nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
    #print( name_rec )
    #print( nn )
    #print( nsym )
    #print( nso )
    #print( nmo )
    
    ### MO Data: list[ 2D-Numpy Array ] format
    amo = []
    for isym in range( nsym ):
        if ( nso[ isym ]*nmo[ isym ] == 0 ):
            continue
        amo_sym = np.empty( [ nso[ isym ], nmo[ isym ] ], dtype = 'float64', order = 'F' )
        data  = read_record( ifs )
        iptr = 4
        #sys.stderr.write( "read: %4d: %4d, %4d\n" % ( isym, nso[ isym ], nmo[ isym ] ) )
        buff = np.frombuffer( data, dtype = 'float64', count = nso[ isym ] * nmo[ isym ], offset = iptr )
        buff_2d = np.reshape( buff, [ nso[ isym ], nmo[ isym ] ], order = 'F' )
        b2t = buff_2d.transpose()
        amo.append( b2t )
        #for imo in range( nmo[ isym ] ):
        #    amo_sym[ imo ] = np.frombuffer( data, dtype = 'float64', count = nso[ isym ], offset = iptr + 8 * nso[ isym ] * imo )
        #amo.append( amo_sym )

    ifs.close()
    return name_rec, nsym, nso, nmo, amo

##################################################################
##################################################################
##################################################################
def write38( fname, amo ):
    irecord = 1
    
    iofs = open( fname, 'r+b' )
    nso  = np.empty( [ 20 ], dtype = np.int32 )
    nmo  = np.empty( [ 20 ], dtype = np.int32 )
    
    ###
    ### Skip Unnecessary Records
    ###
    for irec in range( 1, irecord ):
        data  = read_record( iofs )
        name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
        nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
        nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
        nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
        nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
        for i in range( nsym ):
            if ( nso[ i ]*nmo[ i ] == 0 ):
                continue
            data  = read_record( iofs )
        nsym = 0
    
    ###
    ### Read Required Records
    ###
    ### Basic Data
    data  = read_record( iofs )
    name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
    nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
    nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
    nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
    nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
    #print( name_rec )
    #print( nn )
    #print( nsym )
    #print( nso )
    #print( nmo )
    
    ### MO Data: list[ 2D-Numpy Array ] format
    for isym in range( nsym ):
        if ( nso[ isym ]*nmo[ isym ] == 0 ):
            continue
        bytebuf = bytes()
        bytebuf += struct.pack( 'i', isym )
        bytebuf += amo[ isym ].tobytes()
        #sys.stderr.write( "write: %4d: %4d, %4d\n" % ( isym, nso[ isym ], nmo[ isym ] ) )
        write_record( iofs, bytebuf, 4 + 8 * nso[ isym ] * nmo[ isym ] )
        #for imo in range( nmo[ isym ] ):
        #    amo_sym[ imo ] = np.frombuffer( data, dtype = 'float64', count = nso[ isym ], offset = iptr + 8 * nso[ isym ] * imo )
        #amo.append( amo_sym )

    iofs.close()

