# -*- coding: utf-8 -*-

time = 13
power = False

def engine_room():
    if power == False:
        print "\nVe strojovně se nachází pouze vypnutý motor a počítačová konzole. Na displayi konzole vidíš, že palivový článek je úplně prázdný a běží pouze nouzové funkce systému ze záložní baterie. Ze strojovný vedou dvoje dveře do skladů č. 1 a 2. Co uděláš?\n"
        def fuel_change():
            global power
            global time
            print "Vyměnil si palivový článek a restartoval systém.\nŠtíty se snad začnou regenerovat o něco rychleji.\n"
            game_running()
            power = True
            engine_room()
            
        def what(length):
            print "1. Půjdu do skladu č. 1"
            print "2. Půjdu do skladu č. 2"
            print "3. Vyměním palivový článek a restartuji systém\n"
            action = raw_input("> ")
            if action == "1":
                game_running()
                depot_1()
            elif action == "2":
                game_running()
                depot_2()
            elif action == "3":
                game_running()
                fuel_change()
            else:
                game_running()
                print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
                what(3)

        what(3)
        
    else:
        print "Ve strojovně je jemně bzučící motor a na počítačové konzoli vidíš, že celý energetický systém je v pořádku. Ze strojovny vedou dveře do skladů č. 1 a č. 2. Co uděláš?\n"
        def what(length):
            print "1. Půjdu do skladu č. 1"
            print "2. Půjdu do skladu č. 2"
            action = raw_input("> ")
            if action == "1":
                game_running()
                depot_1()
            elif action == "2":
                game_running()
                depot_2()
            else:
                game_running()
                print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
                what(2)
        
        what(2)
        
def depot_1():
    print "\nJseš ve skladu č. 1. Ze skladu vedou troje dveře. Do strojovny, do skladu č. 2 a do ubikací. Co uděláš?\n"
    def what(length):
        print "1. Půjdu do strojovny"
        print "2. Půjdu do vedlejšího skladu"
        print "3. Půjdu do ubikací\n"
        action = raw_input("> ")
        if action == "1":
            game_running()
            engine_room()
        elif action == "2":
            game_running()
            depot_2()
        elif action == "3":
            game_running()
            dormitory()
        else:
            game_running()
            print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
            what(3)
    
    what(3)

def depot_2():
    print "\nJseš ve skladu č. 2. Ze skladu vedou troje dveře. Do strojovny, do skladu č. 1 a do ubikací. Co uděláš?\n"
    def what(length):
        print "1. Půjdu do strojovny"
        print "2. Půjdu do vedlejšího skladu"
        print "3. Půjdu do ubikací\n"
        action = raw_input("> ")
        if action == "1":
            game_running()
            engine_room()
        elif action == "2":
            game_running()
            depot_1()
        elif action == "3":
            game_running()
            dormitory()
        else:
            game_running()
            print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
            what(3)
    
    what(3)

def dormitory():

    print "\nNacházíš se v ubikacích. Jsou tu dvě postele, stůl, pár židlí, malá koupelna a kuchyňka. Z ubikací se můžeš dostat do obou skladů a do pilotní kabiny. Co uděláš?\n"
    def what(length):
        print "1. Půjdu do skladu č. 1"
        print "2. Půjdu do skladu č. 2"
        print "3. Půjdu do pilotní kabiny\n"
        action = raw_input("> ")
        if action == "1":
            game_running()
            depot_1()
        elif action == "2":
            game_running()
            depot_2()
        elif action == "3":
            game_running()
            bridge()
        else:
            game_running()
            print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
            what(3)
    
    what(3)

def bridge():
    if power == False:
        print "Jsi v pilotní kabině, ale nic toho tady bez 'šťávy' nezmůžeš. Z pilotní kabiny můžeš jít jen do ubikací. Co uděláš?\n"
        def what(length):
            print "1. Půjdu do ubikací"
            action = raw_input("> ")
            if action == "1":
                game_running()
                dormitory()
            else:
                game_running()
                print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
                what(1)
        
        what(1)
        
    else:
        print "Jsi v pilotní kabině. Všechny kontrolky blikají červeně. Počítač automaticky zaměřil dva cíle. Po pohledu na jejich projekci na monitoru je vůbec nepoznáváš. Velikostí jsou něco mezi fregatou a křizníkem. Přemýšlýš kdo to vůbec je a jak to, že tu ještě není policie, když si v zabezpečeném sektoru souhvězdí Harua?\nZ pilotní kabiny vedou pouze dveře do ubikací. Co uděláš?\n"
        
        def communication():
            print "\nNa chvíli ustala palba, ale trvalo to jen pár vteřin, kdy si se dočkal odpovědi - opětovné palby z jejich laserů. Co uděláš?\n"
            what(3)
            
        def shoot_rockets():
            print "Vypálil si naváděné střely z obou dostupných raketometů na tvých křídlech. Na každou loď jednu. První zásah nepřátelskou loď kriticky poškodil a druhá okamžitě explodovala!\nPřeživší loď okamžitě přestala střílet a zmizela nadsvětelnou rychlostí neznámo kam.\n\nVÝBORNĚ!!! Právě jsi dohrál první epizodu!"
            exit(0) 
        
        def what(length):
            print "1. Půjdu do ubikací"
            print "2. Pokusím se navázat komunikaci s nepřátelskými loděmi"
            print "3. Zaútočíš raketami"
            action = raw_input("> ")
            if action == "1":
                game_running()
                dormitory()
            elif action == "2":
                communication()
            elif action == "3":
                game_running()
                shoot_rockets()
            else:
                game_running()
                print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
                what(3)
                
        what(3)
        
def start():
    print "Ahoj pilote,\nvítej v tomto skvělém vesmírném dobrodružství, které právě začíná!\n\n"

    print "Probudil tě otřes celou lodí. Místnost kolem tebe osvětluje pouze blikající červené světlo, ale ihned poznáváš jeden ze dvou skladů na své frigatě. Vůbec netušíš, proč si zrovna tady. Poslední co si pamatuješ, je, že jsi byl v pilotní kabině a sensory zachytily nějakou kosmickou anomálii. Z reproduktorů se ozývá počítač: 'Štíty na 80 %!'.\nJe ti jasné, že musíš jednat a to rychle. Kromě nárazů laserů do štítu neslyšíš nic. Motor je mimo provoz.\nZe skladu vedou troje dveře. Do strojovny, do druhého skladu a do ubikací, ze kterých se můžeš dostat do pilotní kabiny. Co uděláš?\n"
    def what(length):
        print "1. Porozhlédnu se po skladu"
        print "2. Půjdu do strojovny"
        print "3. Půjdu do vedlejšího skladu"
        print "4. Půjdu do ubikací\n"
        action = raw_input("> ")
        if action == "1":
            game_running()
            print "Okolo sebe vidíš pouze hliníkové bedny naplněné ovocem z měsíce planety Turinus IV, které jsi slíbil doručit do malebné hospůdky tvého strýce na planetě Roks II. Na tohle opravdu nemáš čas!"
            depot_1()
        elif action == "2":
            game_running()
            engine_room()
        elif action == "3":
            game_running()
            depot_2()
        elif action == "4":
            game_running()
            dormitory()
        else:
            game_running()
            print "Zadej číslovku od 1 do %d a neztrácej čas!" % length
            what(4)
            
    
    what(4)   
    
def game_running():
    global time
    if power == True:
        time = time - 1
    else:
        time = time - 2
        
    if time == 8:
        print "\n'Štíty na 80 %!'\n"
    elif time == 7:
        print "\n'Štíty na 70 %!'\nKaždou chvílí slyšíš náraz laseru do štítu a následně cítíš mírný otřes.\n"
    elif time == 6:
        print "\n'Štíty na 60 %!'\n"
    elif time == 5:
        print "\n'Štíty na 50 %!'\nDalší rána a otřes je tentokrát o něco silnější!\n"
    elif time == 4:
        print "\n'Štíty na 40 %!'\nPospěš si!\n"
    elif 1 <= time <= 3:
        print "\n'Štíty na kritické úrovni!'\nMusíš si pospíšit!\n"
    elif time == 0:
        print "\nZ reproduktorů se ozvalo: 'Štíty prolomeny!' a za pár vteřin loď vybuchuje\n\nGAME OVER\n\nZkus hru znovu a být rychlejší..."
        exit(0)


start()
