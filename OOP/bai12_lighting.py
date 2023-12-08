class Battery:
    def __init__(self, energy):
        self.energy = energy
    
    def set_energy(self, new_battery):
        energy = new_battery
        print("Pin của đèn đã được thay đổi")
    def get_energy (self):
        return self.energy
    def Decrease_Energy(self,solve):
        if self.energy >= solve:
            self.energy -= solve
            return True
        else:
            print("Hết năng lượng")
            return False
    
    
        
        
class FlashLamp:
    def __init__(self, battery):
        self.battery = battery
        self.turned_on = False
        
    def turn_on(self):
        if self.turned_on:
            print("Đèn đã được bật")
        else:
            if self.battery.Decrease_Energy(1):
                self.turned_on = True
                print("Đèn đã được bật")
                
                
                
    def turn_off(self):
        if not self.turned_on:
            print("Đèn đã tắt")
            
        else:
            self.turned_on = False
            print("Đèn đã được tắt")
            
class TestFlashLamp:
    def main(self):
        # Tạo đối tượng Pin với 10 đơn vị năng lượng
        pin = Battery(10)


        # Tạo đối tượng Đèn và lắp pin vào đèn
        lamp = FlashLamp(pin)
        
        # Bật và tắt đèn pin 10 lần
        for i in range(10):
            print(f"\nLần thử số {i + 1}:")
            
            lamp.turn_on()
            lamp.turn_off()

   
        print(f"\nMức năng lượng còn lại trong pin: {pin.get_energy()}")

# Tạo đối tượng TestFlashLamp và chạy phương thức main()
test_flashlamp = TestFlashLamp()
test_flashlamp.main()
            
            
