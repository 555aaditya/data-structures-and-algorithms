# 605. Can Place Flowers

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    
    for i in range(len(flowerbed)):
        left = 0 if(i == 0) else flowerbed[i-1]
        right = 0 if(i == len(flowerbed) - 1) else flowerbed[i+1]

        if left == 0 and right == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1

    return n <= 0

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1,0,0]
    n = 2

    print(canPlaceFlowers(flowerbed, n))