import astropy.io.fits
import pandas
import tqdm


if __name__=="__main__":
    database = astropy.io.fits.open("/Users/tanimoto/software/heasoft/heasoft-6.29/ftools/xstar/data/atdb.fits")
    pointer  = database[1].data[0][0]
    real     = database[2].data[0][0]
    integer  = database[3].data[0][0]
    string   = database[4].data[0][0]

    Z             = []
    Ion           = []
    Level         = []
    N             = []
    L             = []
    S             = []
    J             = []
    Energy        = []
    Potential     = []
    Configuration = []
    
    for i in tqdm.tqdm(range(len(pointer)//10)):
        if pointer[10*i+1]==6:
            Z.append(integer[pointer[10*i+8]+2])
            Ion.append(integer[pointer[10*i+8]+4])
            Level.append(integer[pointer[10*i+8]+3])
            N.append(integer[pointer[10*i+8]-1])
            L.append(integer[pointer[10*i+8]+1])
            S.append(integer[pointer[10*i+8]+0])
            J.append(int(real[pointer[10*i+7]+0]))
            Energy.append("{0:.4e}".format(real[pointer[10*i+7]-1]))
            Potential.append("{0:.4e}".format(real[pointer[10*i+7]+2]))
            Configuration.append("".join(list(map(chr, string[pointer[10*i+9]-1:pointer[10*i+19]-1]))))

    df = pandas.DataFrame(data={"Z": Z, "Ion": Ion, "Level": Level, "N": N, "L": L, "2S+1": S, "2J+1": J, "Energy": Energy, "Potential": Potential, "Configuration": Configuration})
    print(df)