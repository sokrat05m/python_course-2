# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = 30
petya = S // 6
seryozha = petya
katya = (seryozha + petya) * 2
print (f"Катя сделала {katya} журавликов, а Петя и Сережа по {petya}")