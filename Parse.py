
def parseResources(results):
    if (results['title'] == ""):
        results['title'] = None
    print((results['X1'].isdigit()))
    if ((results['X1'].isdigit()) or not (results['X1'] =='')):
        results['X1'] = int(results['X1'])
    else :
        results['X1'] = None
    if ((results['X10'].isdigit()) or not (results['X10'] =='')):
        results['X10'] = int(results['X10']) 
    else :
        results['X10'] = None
    if ((results['X100'].isdigit()) or not (results['X100'] =='')):
        results['X100'] = int(results['X100'])
    else :
        results['X100'] = None

    return results

if __name__ == "__main__":
    pass
