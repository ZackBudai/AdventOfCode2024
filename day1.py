with open("day1.txt", "r") as txt_file:
  contents = txt_file.read().splitlines()

contents = [line.split("   ") for line in contents]

list1 = [i[0] for i in contents]
list2 = [i[1] for i in contents]
sortedlist1 = sorted(list1)
sortedlist2 = sorted(list2)

differenceTotal = 0
similarityTotal = 0

for idx in range(len(sortedlist1)):
   differenceTotal += abs(int(sortedlist1[idx])-int(sortedlist2[idx]))


for idx in range(len(sortedlist1)):
    count = 0
    for el in sortedlist2:
       if sortedlist1[idx] == el:
          count += 1
    similarityTotal += int(sortedlist1[idx])*count

print(differenceTotal)
print(similarityTotal)