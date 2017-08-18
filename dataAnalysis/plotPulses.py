import sys
import ROOT
import tdrstyle
tdrstyle.setTDRStyle()
ROOT.gStyle.SetPadRightMargin(0.08);
ROOT.gStyle.SetOptFit(0 );
ROOT.gStyle.SetPalette(55);
import math
from array import array
import os


##---------------------------------------
def main():

	# analyze these files
	idir = "/Users/ntran/Dropbox/NeutronBANJA";
	files = [];
	files.append(idir + "/" + "20170810_r580_BC702_Am241_test3.root");
	# files.append(idir + "/" + "20170513_rXXX_polystyrene_bismuth207.root");
	# files.append(idir + "/" + "20170513_rXXX_polystyrene_bismuth207-moreVoltage.root");
	# files.append(idir + "/" + "20170712_r580_950V_dc702_foil-down_bismuth207.root");
	# files.append(idir + "/" + "20170712_r580_dc702_bismuth207.root");
	# files.append(idir + "/" + "20170712_r580_gs20_bismuth207.root");
	# files.append(idir + "/" + "20170712_r580_gs20_foil-down_bismuth207.root");
	# files.append(idir + "/" + "20170712_r580_gs20_foil-up_bismuth207_v2.root");
	# files.append(idir + "/" + "20170712_r580_gs20_foil-up_bismuth207_v3.root");
	# files.append(idir + "/" + "20170712_r580_gs20_foil-up_bismuth207_v4.root");
	# files.append(idir + "/" + "20170712_r580_gs20_foil-up_bismuth207_v5.root");
	# files.append(idir + "/" + "20170712_r580_polystyrene_bismuth207.root");	
 
	for f in files:
		fin = ROOT.TFile(f);
		tag = os.path.splitext( os.path.basename(f) )[0];
		print tag;
		analyze(fin, tag);

def analyze(fin, tag):

	tin = fin.Get("T");
	h_pulse = ROOT.TH1F("h_pulse",";integrated pulse; events", 100, -10, 0);

	nent = tin.GetEntries();
	for i in range(nent):
	
		if(nent/100 > 0 and i % (1 * nent/100) == 0):
			sys.stdout.write("\r[" + "="*int(20*i/nent) + " " + str(round(100.*i/nent,0)) + "% done")
			sys.stdout.flush()

		tin.GetEntry(i);

		cursum = 0;
		for it in range(450,550):
			cursum += tin.c1[it];
		h_pulse.Fill(cursum);

	ctmp = ROOT.TCanvas("ctmp","ctmp",1000,800);
	h_pulse.Draw();
	ctmp.SaveAs("plots/pulse_%s.pdf" % (tag));
	ctmp.SaveAs("plots/pulse_%s.png" % (tag));

##---------------------------------------
if __name__ == '__main__':
		main();
##---------------------------------------     