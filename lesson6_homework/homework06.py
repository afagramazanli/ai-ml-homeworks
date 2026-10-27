import numpy as np

names = ["Aysel", "Murad", "Nigar", "Orxan", "Leyla"]

scores = np.array([
    [72, 80, 88],
    [60, 74, 68],
    [95, 91, 89],
    [45, 55, 65],
    [82, 78, 84]
])


# Task 1 - Array Properties


print(f'number of students: {scores.shape[0]}' )

print(f"number of exams: {scores.shape[1]}")

print(f"total values: {scores.size}")

print(f"Dimensions: {scores.ndim}")

print(f"Data type: {scores.dtype}")


# Task 2: Indexing

print(f"Ayselin birinci imtahan bali: {scores[0, 0]}")
print(f"Muradin ucuncu imtahan bali: {scores[1, 2]}")
print(f"Nigarin ikinci imtahan bali: {scores[2, 1]}")
print(f"Leylanin sonuncu imtahan bali: {scores[4, 2]}")
print(f"Orxanin butun imtahan neticeleri: {scores[3]}")
print(f"Sonuncu telebenin sonuncu imtahan bali: {scores[-1, -1]}")

#  Task 3: slicing

print("Ilk 3 telebenin butun imtahan neticeleri:", scores[0:3])

print("Son 2 telebenin butun imtahan neticeleri:", scores[-2:])

print("Butun telebelerin birinci imtahan neticeleri:", scores[:, 0])

print("Butun telebelerin ucuncu imtahan neticeleri:", scores[:, 2])
print("Ilk 3 telebenin ikinci ve ucuncu imtahan neticeleri:", scores[0:3, 1:3])

print("Murad ve Nigarin butun imtahan neticeleri:", scores[1:3, :])

task3_result = scores[0:3, 1:3]
print("5-ci bendin shape deyeri:", task3_result.shape)


updated_scores = scores + 5
print(updated_scores)

print("Butun ballardan 10 cix:", scores - 10)
print("Butun ballari 2-ye bol:", scores / 2)
print("Butun ballari 2-ye vur:", scores * 2)
print("Exam 2 - Exam 1:", scores[:, 1] - scores[:, 0])
print("Exam 3 - Exam 2:", scores[:, 2] - scores[:, 1])
print("Original scores:", scores)

print("70-den kicik ballar:", scores[scores < 70])
print("70 ve daha yuxari ballar:", scores[scores >= 70])
print("90 ve daha yuxari ballar:", scores[scores >= 90])


print("50-den kicik ballar:", scores[scores < 50])

print("80-den boyuk ballar:", scores[scores > 80])

print("70-den kicik ballarin sayi:", np.sum(scores < 70))

print("70 ve daha yuxari ballarin sayi:", np.sum(scores >= 70))

print("90 ve daha yuxari ballarin sayi:", np.sum(scores >= 90))

print("50-den kicik ballarin sayi:", np.sum(scores < 50))

print("80-den boyuk ballarin sayi:", np.sum(scores > 80))

#task 6

print("Butun ballarin cemi:", np.sum(scores))
print("Butun ballarin ortalamasi:", np.mean(scores))
print("En yuksek bal:", np.max(scores))
print("En asagi bal:", np.min(scores))
print("Ballarin mediani:", np.median(scores))
print("Ballarin araligi:", np.max(scores) - np.min(scores))

print("Orta baldan yuxari olan ballar:", scores[scores > np.mean(scores)])
print("Orta baldan yuxari ballarin sayi:", np.sum(scores > np.mean(scores)))

# task 7 

print("Her telebenin orta bali:", np.mean(scores, axis=1))

print("Her imtahanin orta bali:", np.mean(scores, axis=0))

print("Her telebenin en yuksek bali:", np.max(scores, axis=1))

print("Her telebenin en asagi bali:", np.min(scores, axis=1))

print("Her imtahanda en yuksek bal:", np.max(scores, axis=0))

print("Her imtahanda en asagi bal:", np.min(scores, axis=0))

print("Her telebenin umumi bali:", np.sum(scores, axis=1))

# task 8

averages=np.mean(scores,axis=1)

print(f"her telebenin orta bali: {averages}")
print(f"orta bali 75 ve daha yuxari olan telebeler: {np.array(names)[averages>= 75]} ")
print(f'orta bali 75 ve daha yuxari olan telebelerin sayi: {np.sum(averages>=75)}')
print(f"Orta bali 75-den asagi olan telebelerin sayi: {np.sum(averages < 75)}")

print(f"Orta bali 85-den yuxari olan telebelerin butun ballari: {scores[averages > 85]}")

print(f"En yuksek telebe ortalamasi: {np.max(averages)}")