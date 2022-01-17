import astropy.io.fits
import pandas
import tqdm


if __name__=="__main__":
    database = astropy.io.fits.open("/Users/tanimoto/software/heasoft/heasoft-6.29/ftools/xstar/data/atdb.fits")
    pointer  = database[1].data[0][0]
    real     = database[2].data[0][0]
    integer  = database[3].data[0][0]
    string   = database[4].data[0][0]

    Z           = []
    Lower_Ion   = []
    Lower_Level = []
    Upper_Ion   = []
    Upper_Level = []
    N           = []
    L           = []
    S           = []
    Energy      = []
    Cross       = []

    for i in range(len(pointer)//10):
        if pointer[10*i+1]==70:
            nd = integer[pointer[10*i+8]-1]
            nt = integer[pointer[10*i+8]+0]
            nx = integer[pointer[10*i+8]+1]

            for j in range(nx):
                Z.append(integer[pointer[10*i+8]+5])
                Lower_Ion.append(integer[pointer[10*i+8]+7])
                Lower_Level.append(integer[pointer[10*i+8]+6])
                Upper_Ion.append(integer[pointer[10*i+8]+9])
                Upper_Level.append(integer[pointer[10*i+8]+8])
                N.append(integer[pointer[10*i+8]+2])
                L.append(integer[pointer[10*i+8]+3])
                S.append(integer[pointer[10*i+8]+4])
                Energy.append("{0:.4e}".format(0.013605*real[pointer[10*i+7]+nd+nt+nd*nt+2*j-1]))
                Cross.append("{0:.4e}".format(real[pointer[10*i+7]+nd+nt+nd*nt+2*j+0]))

    df = pandas.DataFrame(data={"Z": Z, "Lower_Ion": Lower_Ion, "Lower Level": Lower_Level, "Upper_Ion": Upper_Ion, "Upper Level": Upper_Level, "N": N, "L": L, "2S+1": S, "Energy (keV)": Energy, "Cross Section (Mb)": Cross})
    df = df.sort_values(["Z", "Lower_Ion"])
    df = df.reset_index(drop=True)
    df.to_html("sample.html")