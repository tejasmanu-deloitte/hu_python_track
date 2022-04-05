sampleDict = {'name': "Kelly",
              'age': 25,
              'salary': 8000,
              'city': "New york"
              }

print("Initial Dictionary", sampleDict)

sampleDict['Location'] = sampleDict.pop('city')
print("Final Dictionary", str(sampleDict))