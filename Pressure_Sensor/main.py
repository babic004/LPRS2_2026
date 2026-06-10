from pressure_sensor import *
import pressure_sensor_enum as pse

if __name__== "__main__":
    sensor = PressureSensor(port="/dev/ttyUSB0", highLimit = 6, lowLimit=5.0, targetValue = 5.5, mode=pse.WorkingMode.WINDOW_COMPARATOR, unit = pse.Units.BAR, measureLogic= pse.MeasureLogic.POSITIVE)

    while(1):
        sensor.getCurrentValue()
        sensor.getLowLimit()
        sensor.getHighLimit()
        sensor.getTargetValue()
        sensor.getHighLimit()
        sensor.getLowLimit()
        sensor.getNPNStatus()
        print("-" * 50)
        time.sleep(5)        
    
    #sensor.getTargetValue()
