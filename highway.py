# Highways
Purpose: determine a highway while only typing in a number

  def highway_info(highway_number):
    if highway_number < 1 or highway_number > 999 or (highway_number > 99 and highway_number % 100 == 0):
        return f"{highway_number} is not a valid interstate highway number."
    if highway_number < 100:
        direction = "north/south" if highway_number % 2 == 1 else "east/west"
        return f"I-{highway_number} is primary, going {direction}."
    else:
        primary_highway = highway_number % 100
        direction = "north/south" if primary_highway % 2 == 1 else "east/west"
        return f"I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}."

if __name__ == '__main__':
    highway_number = int(input("Enter highway number: "))
    print(highway_info(highway_number))
