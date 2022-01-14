import astropy.io.fits
import pandas
import tqdm


if __name__=="__main__":
    database = astropy.io.fits.open("/Users/tanimoto/software/heasoft/heasoft-6.29/ftools/xstar/data/atdb.fits")
    pointer  = database[1].data[0][0]
    real     = database[2].data[0][0]
    integer  = database[3].data[0][0]
    string   = database[4].data[0][0]

    Z            = []
    Ion          = []
    InitialLevel = []
    FinalLevel   = []
    Energy       = []
    Strength     = []
    Coefficient  = []

    for i in tqdm.tqdm(range(len(pointer)//10)):
        if pointer[10*i+1]==50 or pointer[10*i+1]==82:
            if 0<float(real[pointer[10*i+7]-1]):
                Z.append(integer[pointer[10*i+8]+1])
                Ion.append(integer[pointer[10*i+8]+2])
                InitialLevel.append(integer[pointer[10*i+8]+0])
                FinalLevel.append(integer[pointer[10*i+8]-1])
                Energy.append("{0:.4e}".format(12398/float(real[pointer[10*i+7]-1])))
                Strength.append("{0:.4e}".format(real[pointer[10*i+7]+0]))
                Coefficient.append("{0:.4e}".format(real[pointer[10*i+7]+1]))

    df = pandas.DataFrame(data={"Z": Z, "Ion": Ion, "Initial Level": InitialLevel, "Final Level": FinalLevel, "Energy": Energy, "Strength": Strength, "Coefficient": Coefficient})
    df = df.sort_values(["Ion", "Initial Level"])
    df = df.reset_index(drop=True)
    print(df)