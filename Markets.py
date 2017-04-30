import Read
import Check
import Parse
import DbManagement
import Settings 



marketsToDb = {
    'Resources':DbManagement.addResources,
    'Miner':DbManagement.addMiner,
    'RollBack':DbManagement.rollBack,
    'commitDB':DbManagement.commitDB,
}

def launch(market):
    results = []
    if(market in ['Resources','Miner']):
        results.extend(Read.readingFrom(Settings.settings['Markets']['location']['otype'],Settings.settings['Read']['mode']['texte'],method='single_textline',colors=['gray'])) 
        results.extend(Read.readingFrom(Settings.settings['Markets']['location']['title'],Settings.settings['Read']['mode']['texte'],method='single_textline',))
        results.extend(Read.readingFrom(Settings.settings['Markets']['location']['un'],Settings.settings['Read']['mode']['kamas'],method='only_digits',))
        results.extend(Read.readingFrom(Settings.settings['Markets']['location']['dix'],Settings.settings['Read']['mode']['kamas'],method='only_digits',))
        results.extend(Read.readingFrom(Settings.settings['Markets']['location']['cent'],Settings.settings['Read']['mode']['kamas'],method='only_digits',))
              
        results = Check.checkResources(results)
        results = Parse.parseResources(results)
        marketsToDb[market](results)
        
        return results
    elif(market == 'RollBack'):
        marketsToDb['RollBack']()
    elif(market == 'commitDB'):
        marketsToDb['commitDB']()
        

if __name__ == "__main__":
    pass
