from prac_6.guitar import Guitar

def main():
    gibsonL5ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    gretsch6128duojet = Guitar("Gretsch 6128 Duo Jet", 1963, 7581.99)
    fenderstatocaster = Guitar("Fender Stratocaster", 2014, 765.40)

    my_guitars = [gibsonL5ces, gretsch6128duojet, fenderstatocaster]
    for guitar in my_guitars:
        guitar.get_age()
        if guitar.is_vintage():
            return True

main()

