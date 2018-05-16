from collections import Counter


def counter():
    words = []
    results = []
    string = input("Bitte geben Sie ihren DNA-Strang ein.")  #Abfrage des DNA-Stranges vom Benutzer
    k = int(input("Bitte geben Sie die Länge des k-mers ein. "))  #Abfrage der Länge des k-mers vom Benutzer

    for i in range(len(string)):
        words.append("".join(string[i: i+k]))
        tuples = Counter(words).most_common()
        max_count = max([y for (x, y)in tuples])

    for (x,y) in tuples:
        if y == max_count:
            results.append(x)
    return results

print (counter()) #Ausgabe der am häufigsten vorkommenden k-mere