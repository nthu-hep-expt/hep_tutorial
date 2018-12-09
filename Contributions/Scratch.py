import sys
sys.path.append('/afs/cern.ch/work/w/will/public/indicomb')

from indicomb import indicomb

indicomb( headerHTML="<center><h1>Contributions from Meng-Ju Tsai</h1></center><link rel='stylesheet' type='text/css' href='style.css'>",
                 #"<center><h2>NTHU Group Meetings</h2></center>",
                 output="/eos/user/m/metsai/www/meeting/Meng-Ju-Contributions.html",
                 #includeList=["CalRatio","EXOT-2017-20","EXOT-2017-26","EXOT-2017-05","EXOT-2017-28","EXOT-2017-24","EXOT-2017-03"],
                 #includeList=["ggF+VBF"],
                 includeList=["R21 Migration Effort Discussion", "ggF+VBF analysis meeting", "NTHU Group Meeting", "HWW weekly meeting", "ATLAS H - WW Workshop" ],
                 excludeList=["CANCELLED","CANCELED"],
                 speakerList=["Meng-Ju"],
                 startDate="2016-04-01",
                 endDate="2018-08-10",
                 categoryNumbers=[8790, 8242, 9447, 6420, 2322])
                 #categoryNumbers=[8242])
