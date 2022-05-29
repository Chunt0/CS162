# Christopher Hunt
# CS162
# driver.py

from arena import Arena

def main():
    battle = Arena()
    print(f"##Player##\n{battle.player}")
    print(f"##Comp##\n{battle.comp}")
    battle.menu()

if __name__ == "__main__":
    main()
