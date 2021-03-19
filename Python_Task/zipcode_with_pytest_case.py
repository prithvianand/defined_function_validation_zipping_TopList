def ZipCode(KeyList,ValueList):
    Dict = {} # Create A dictionary
    #if both the list atre of same length  or Key List is smaller
    if(len(KeyList)==len(ValueList) or len(ValueList)>len(KeyList)): #if both the list atre of same length  or Key List is smaller
        for i in range(len(KeyList)):
            Dict[KeyList[i]] = ValueList[i]
    elif(len(KeyList)>len(ValueList)): # if Value List has less numbers
        for i in range(len(ValueList)):
            Dict[KeyList[i]] = ValueList[i]
        for j in range(i+1,len(KeyList)):
            Dict[KeyList[j]] = "None"
    return Dict


## Test

# SameLength Lists
def test_Samlength():
    GroundDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    Key = ["a","b","c","d","e","f"]
    Val = [1,2,3,4,5,6]
    assert  GroundDict== ZipCode(Key,Val)

# Key > Value Lists
def test_KeyLenisMore():
    GroundDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 'None', 'h': 'None'}
    Key = ["a","b","c","d","e","f","g","h"]
    Val = [1,2,3,4,5,6]
    assert GroundDict == ZipCode(Key,Val)

# Value > key Lists
def test_KeyLenisSmall():
    GroundDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    Key = ["a","b","c","d","e","f"]
    Val = [1,2,3,4,5,6,7,8,9]
    assert GroundDict== ZipCode(Key,Val)