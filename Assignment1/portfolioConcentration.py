#import the csv module
import csv

class PortfolioConcentration(object):
    
    #open a comma delimited file and return the output
    #I wrote this function so that it takes any column and returns the sum of market value by that column    
    def GetMeasureTotalBySlice(self, slice, measure):
        try:
            positionsFile = None
            # raw string
            fileName = r".\PortfolioAppraisalReport.csv"
            if not csv.Sniffer().has_header(fileName):
                raise Exception("headers expected in position file. FileName: " + fileName)
            positionsFile = open(fileName, 'rt')
            dictReader = csv.DictReader(positionsFile)
            #dictReader is list of dictionaries where the keys are the column headers and the values represent one row of values
            
            dictTag = {}
            #iterate over 
            for dictRow in dictReader:
                mv = dictRow[measure]
                strat = dictRow[slice]
                #need to cast to float
                if(dictTag.has_key(strat)):
                    dictTag[strat] += float(mv)
                else:
                    dictTag[strat] = float(mv)
            return dictTag
        except Exception, e:
            print e
            raise e
        finally:
            #print 'Finalizer called'
            if positionsFile != None :
                positionsFile.close()
     
    #This function should accept the dictionary and return that max and the min value in the dictionary
    def GetTopandBottomSlices(self, sliceData):
        #open a comma delimited file and return the output
        #it takes any column and returns the min and max number by that column    
        try:
            positionsFile = None
            # raw string
            fileName = r".\PortfolioAppraisalReport.csv"
            if not csv.Sniffer().has_header(fileName):
                raise Exception("headers expected in position file. FileName: " + fileName)
            positionsFile = open(fileName, 'rt')
            dictReader = csv.DictReader(positionsFile)
            #dictReader is list of dictionaries where the keys are the column headers and the values represent one row of values
            MaxRow={}
            MinRow={}
            max=0
            min=0
            #iterate over 
            for dictRow in dictReader:
                datanum = float(dictRow[sliceData])
                #print datanum
                #need to cast to float
                if(datanum > max):
                    MaxRow = dictRow
                    max = datanum
                elif(datanum < min):
                    MinRow = dictRow
                    min = datanum
                else:
                    continue
            #MaxnMin={'max':max,'min':min,'max'}
            return MinRow,MaxRow
        except Exception, e:
            print e
            raise e
        finally:
            #print 'Finalizer called'
            if positionsFile != None :
                positionsFile.close()                
        return "Complete the implementation"
        
try:
    #how do you want to query this portfolio
    slice = "StrategyDesc"
    measure = "BaseMarketValue"
    portfolioConcentration = PortfolioConcentration()
    tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure) 
    #print '\n'
    print tagData
    #calculate the exposure to value equities
    Sum=tagData["Bonds"]+tagData["Event Equities"]+tagData["HEDGE-Other"]+tagData["Bank Debt"]+tagData["Value Equities"]+tagData["Other Equities"]+tagData["Equity Index Hedges"]+tagData["CDS (notional)"]
    ExpoValueEqui=tagData["Value Equities"]/Sum
    print "the exposure to value equities is ",ExpoValueEqui
    #calculate the biggest short and long position
    biglong={}
    bigshort={}
    #portfolioConcentration = PortfolioConcentration()
    bigshort,biglong=portfolioConcentration.GetTopandBottomSlices("BaseMarketValue")
    print "the biggest short security code  ", bigshort["SecurityCode"]
    print "the biggest short market value   ", bigshort["BaseMarketValue"]
    print "the biggest long security code  ", biglong["SecurityCode"]
    print "the biggest long market value   ", biglong["BaseMarketValue"]
    #calculate the top and bottom performance strategies and asset types
    topperf={}
    bottomperf={}
    bottomperf,topperf=portfolioConcentration.GetTopandBottomSlices("YTDTotalPnL")
    print "top performer YTDTotalPnL    ", topperf["YTDTotalPnL"]
    print "top performer strategy       ", topperf["StrategyCode"]
    print "top performer asset type     ", topperf["StrategyDesc"]
    print "bottom performer YTDTotalPnL ", bottomperf["YTDTotalPnL"]
    print "bottom performer strategy    ", bottomperf["StrategyCode"]
    print "bottom performer asset type  ", bottomperf["StrategyDesc"]
    
except Exception, e:
    print e    
        