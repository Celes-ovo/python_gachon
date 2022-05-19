# class 정의

class Car:
    # 생성된 객체 수를 저장하는 변수
    count = 0

    # 생성자 정의 : init은 객체를 하나 생성할 때마다 자동 호출
    # def __init__(self) -> None: : Return type을 지정해주는 방식. (int, str 등등)

    # self : local 변수로만 쓰게 하지 않고, 다른 곳에서도 변수들을 사용하게 하고 싶을 때 : self
    # self를 정의하면 이후에 self를 쓰지 않아도 자동적으로 따라가게 됨.
    def __init__(self, model) :
        Car.count += 1
        # 위의 count와는 별개
        self.count = 20

        # 인스턴스 변수 : 객체마다 독립적으로 생성됨.
        self.model = model
        print(self.model)

        self.carSpeed = 0

        print(f'생성된 자동차 : {Car.count}대')


    def go(self):
        self.carSpeed += 10
        self.display()


    def display(self):
        print(f'cars speed = {self.carSpeed}')

#############################################################################

c1 = Car('K5')
c2 = Car('Honda')

c1.go()
c2.go()
c2.go()
c2.go()



# c1 자동차의 현재 속도만 출력하려면?
print(f"c1's speed : {c1.carSpeed}", '\n========================')


# count의 차이 보기
print(c1.count)
print(Car.count)


######################################
# subclass 정의

class SportsCar(Car):

    # go를 굳이 정의하지 않아도 동작은 하지만, 서브 클래스에서 다시 정의할 수 있음 : 오버라이딩
    # 다형성을 구현하기 위한 방법 : 부모 클래스가 정의한 것을 다시 정의하기
    def go(self):
        self.carSpeed += 30

        # display는 Car class에 이미 있기 때문에 display를 그대로 사용해도 에러가 나지 않음.
        self.display()

    # 내부에 또다른 기능 역시 추가 가능함.
    def boost(self):
        self.carSpeed += 50
        self.display()


c3 = SportsCar('BMW')
c3.go()
c3.boost()

###################################################

