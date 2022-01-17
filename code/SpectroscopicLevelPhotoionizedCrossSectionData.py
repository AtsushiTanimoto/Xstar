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
    InitialIon   = []
    InitialLevel = []
    FinalIon     = []
    FinalLevel   = []
    N            = []
    L            = []
    J            = []
    Energy       = []
    CrossSection = []

    for i in tqdm.tqdm(range(len(pointer)//10)):
        if pointer[10*i+1]==49 or pointer[10*i+1]==53:
            for j in range(pointer[10*i+4]//2):
                Z.append(integer[pointer[10*i+8]+2])
                InitialIon.append(integer[pointer[10*i+8]+6])
                InitialLevel.append(integer[pointer[10*i+8]+5])
                FinalIon.append(integer[pointer[10*i+8]+4])
                FinalLevel.append(integer[pointer[10*i+8]+3])
                N.append(integer[pointer[10*i+8]-1])
                L.append(integer[pointer[10*i+8]+0])
                J.append(integer[pointer[10*i+8]+1])
                Energy.append("{0:.4e}".format(real[pointer[10*i+7]+2*j-1]))
                CrossSection.append("{0:.4e}".format(real[pointer[10*i+7]+2*j+0]))

    df = pandas.DataFrame(data={"Z": Z, "Initial Ion": InitialIon, "Initial Level": InitialLevel, "Final Ion": FinalIon, "Final Level": FinalLevel, "N": N, "L": L, "2J": J, "Energy (Ry)": Energy, "Cross Section (Mb)": CrossSection})
    print(df)