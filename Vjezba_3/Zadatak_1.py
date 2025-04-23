a=5.0
b=4.935
print(a-b)
#Očekivani rezultat je 0.065, ali Python vraća 0.06500000000000039. Razlika se javlja zbog načina na koji informatičari predstavljaju decimalne brojeve u binarnome sustavu. Broj 4.935 ne može se točno predstaviti u binarnome obliku, što dovodi do malih grešaka u računanju (floating-point aritmetika). Ova su odstupanja normalna u računarstvu i obično su zanemariva, osim u slučajevima kada je potrebna visoka preciznost.

c = 0.1
d = 0.2
e = 0.3
print(c + d + e)
#Ovo odstupanje nastaje zbog načina na koji i informatičari predstavljaju decimalne brojeve u binarnom sustavu. Brojevi poput 0.1 i 0.2 nemaju točan binarni ekvivalent, što dovodi do malih pogrešaka pri računanju (floating-point aritmetika).