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
    InitialLevel  = []
    FinalLevel    = []
    L             = []
    S             = []
    J             = []
    Energy        = []
    Rate          = []
    Configuration = []

    for i in tqdm.tqdm(range(len(pointer)//10)):
        if pointer[10*i+1]==72 or pointer[10*i+1]==75:
            Z.append(integer[pointer[10*i+8]+3])
            Ion.append(integer[pointer[10*i+8]+4])
            InitialLevel.append(integer[pointer[10*i+8]+1])
            FinalLevel.append(integer[pointer[10*i+8]+2])
            L.append(integer[pointer[10*i+8]+0])
            S.append(integer[pointer[10*i+8]-1])
            J.append(int(real[pointer[10*i+7]+1]))
            Rate.append("{0:.4e}".format(real[pointer[10*i+7]-1]))
            Energy.append("{0:.4e}".format(real[pointer[10*i+7]+0]))
            Configuration.append("".join(list(map(chr, string[pointer[10*i+9]-1:pointer[10*i+19]-1]))))

    df = pandas.DataFrame(data={"Z": Z, "Ion": Ion, "Initial Level": InitialLevel, "Final Level": FinalLevel, "L": L, "2S+1": S, "2J+1": J, "Energy": Energy, "Rate": Rate, "Configuration": Configuration})
    print(df)