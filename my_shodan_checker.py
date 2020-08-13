import shodan #importerar shodan modulen

#variabel som öppnar och läser innehållet i text filet
SHODAN_API_KEY = open("key.txt", "r")
#variabel som anropar funktionen från modulen och använder SHODAN_API_KEY variabel från vilken får api nyckel
api = shodan.Shodan(SHODAN_API_KEY)

try: #låter mig testa koden efter errors
    val = input("Search: ") # variabel som tar användares input
    f = open("hi.txt", "w+") # variabel som öppnar och skapar fil om det redo inte existerar
    results = api.search(val) #variabel som använder search funktion från shodan modulen och input från val variabel

    print('Resultaten är: {}'.format(results['total'])) #ger output av hur många resultatet man fick
    for result in results['matches']: #loopar allt under tills det finns ingenting kvar att loopa
        print('IP: {}'.format(result['ip_str'])) #ger output av ip adresser
        print(result['data']) #ger output av olika data
        print('') #skriver ut allt rester
        ip = result['ip_str'] #variabel som hämtar ip adresser
        da = result['data'] #variabel som hämtar data
        land = result['location']['country_name'] #varabel som hämtar länder namn
        on = result['os'] #variabel som hämtar os informationer.
        f.write(str(f"IP: {ip}, Land: {land}, Server: {da}, OS: {on} \r\n")) #skriver data i en text fil

    f.close() #stänger filen och stämmer av att allt data blev sparad i filen
except shodan.APIError as e: #hanterar errors
    print('Error: {}'.format(e)) #skriver ut errors



'''import shodan
SHODAN_API_KEY = open("key.txt", "r")
api = shodan.Shodan(SHODAN_API_KEY)
try:
    val = input("What you want to search: ")
    f = open("hi.txt", "w+")
    results = api.search(val)


    print('Resultaten är: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
        ip = result['ip_str']
        da = result['data']
        land = result['location']['country_name']
        on = result['os']
        f.write(str(f"IP: {ip}, Land: {land}, Server: {da}, OS: {on} \r\n"))
    f.close()

except shodan.APIError as e:
    print('Error: {}'.format(e))'''