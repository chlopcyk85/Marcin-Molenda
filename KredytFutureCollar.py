#wartosci podane przez użytkownia(terminal)
oprocentowanie_kredytu=float(input("Podaj jakie ma być stałe oprocentowanie Twojego kredytu: "))
stala_rata = int(input("Podaj wysokosc stałej raty kredytu: "))
wysokosc_kredytu=int(input("Podaj wartość początkową kredytu, kwota pożyczki: "))
kredyt_na10 = wysokosc_kredytu/10

#wysokosc inflacji na przestrzeni 24 miesiecy
styczen_1 = 1.592824484
luty_1 = -0.453509101
marzec_1 = 2.324671717
kwiecien_1 = 1.261254407
maj_1 = 1.782526286
czerwiec_1 = 2.329384541
lipiec_1 = 1.502229842
sierpien_1 = 1.782526286
wrzesien_1 = 2.328848994
pazdziernik_1 = 0.616921348
listopad_1 = 2.352295886
grudzien_1 = 0.337779545
styczen_2 = 1.577035247
luty_2 = -0.292781443
marzec_2 = 2.48619659
kwiecien_2 = 0.267110318
maj_2 = 1.417952672
czerwiec_2 = 1.054243267
lipiec_2 = 1.480520104
sierpien_2 = 1.577035247
wrzesien_2 = -0.07742069
pazdziernik_2 = 1.165733399
listopad_2 = -0.404186718
grudzien_2 = 1.499708521

#wyliczenia dla kazdego miesiaca (24)
pozyczka_1 = (1+((styczen_1+oprocentowanie_kredytu))/kredyt_na10)*wysokosc_kredytu-stala_rata
pozyczka_2 = (1+((luty_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_1-stala_rata
pozyczka_3 = (1+((marzec_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2-stala_rata
pozyczka_4 = (1+((kwiecien_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_3-stala_rata
pozyczka_5 = (1+((maj_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_4-stala_rata
pozyczka_6 = (1+((czerwiec_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_5-stala_rata
pozyczka_7 = (1+((lipiec_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_6-stala_rata
pozyczka_8 = (1+((sierpien_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_7-stala_rata
pozyczka_9 = (1+((wrzesien_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_8-stala_rata
pozyczka_10 = (1+((pazdziernik_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_9-stala_rata
pozyczka_11 = (1+((listopad_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_10-stala_rata
pozyczka_12 = (1+((grudzien_1+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_11-stala_rata
pozyczka_2_1 = (1+((styczen_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_12-stala_rata
pozyczka_2_2 = (1+((luty_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_1-stala_rata
pozyczka_2_3 = (1+((marzec_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_2-stala_rata
pozyczka_2_4 = (1+((kwiecien_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_3-stala_rata
pozyczka_2_5 = (1+((maj_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_4-stala_rata
pozyczka_2_6 = (1+((czerwiec_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_5-stala_rata
pozyczka_2_7 = (1+((lipiec_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_6-stala_rata
pozyczka_2_8 = (1+((sierpien_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_7-stala_rata
pozyczka_2_9 = (1+((wrzesien_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_8-stala_rata
pozyczka_2_10 = (1+((pazdziernik_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_9-stala_rata
pozyczka_2_11 = (1+((listopad_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_10-stala_rata
pozyczka_2_12 = (1+((grudzien_2+oprocentowanie_kredytu))/kredyt_na10)*pozyczka_2_11-stala_rata

