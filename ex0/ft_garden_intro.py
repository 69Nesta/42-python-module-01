#! python3

def main() -> None:
    """Introduce a plant in the garden."""
    name = "Rose"
    height = 42
    age = 30
    print(f"Plant : {name}\n" +
          f"Height : {height} cm\n" +
          f"Age : {age} days\n")


if __name__ == '__main__':
    print("=== Welcome to My Garden ===")
    main()
    print("=== End of Program ===")
