#Nicholas Larsen Celsius to Fahrenheit

celsiusTemp = input("What is the tempature in Celsius?")
celsiusTemp = int(celsiusTemp)
fahrenheitTemp = (celsiusTemp * 9/5)+32
fahrenheitTemp = str(fahrenheitTemp)
print("When it is", celsiusTemp, "degrees outside, it is", fahrenheitTemp, "degrees fahrenheit")