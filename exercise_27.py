one = True and True
#prints True
print(f"1. {one}")

two = False and True
#prints False
print(f"2. {two}")

three = (1 == 1 and 2 == 1)
#prints False
print(f"3. {three}")

four = "test" == "test"
#prints True
print(f"4. {four}")

five = (1 == 1 and 2 == 1)
#prints False
print(f"5. {five}")

six = True and 1 == 1
#prints True
print(f"6. {six}")

seven = False and 0 != 0
#prints False
print(f"7. {seven}")

eight = True or 1 == 1
#prints True
print(f"8. {eight}")

nine = "test" == "testing"
#prints False
print(f"9. {nine}")

ten = 1 != 0 and 2 == 1
#prints False
print(f"10. {ten}")

eleven = "test" == "testing"
#print False
print(f"11. {eleven}")

twelve = "test" == 1
#print false
print(f"12. {twelve}.")

thirteen = not (True and False)
#prints true
print(f"13. {thirteen}")

fourteen = not (1==1 and 0 !=1)
#prints false
print(f"14. {fourteen}")

fifteen = not(10 == 1 or 1000 == 1000)
#prints False REM or
print(f"15. {fifteen}")

sixteen = not (1 != 10 or 3 == 4)
#prints False
print(f"16. {sixteen}")

seventeen = not ("testing == testng" and "Zed" == "Cool Guy")
#prints True
print(f"17. {seventeen}")

eighteen = 1 == 1 and (not("testing" == 1 or 1 == 0))
#eighteen = true and not(false)
#prints True
print(f"18. {eighteen}")

nineteen = "chunky" == "bacon" and (not(3 == 4 or 3 == 3))
#nineteen = false and not(true)
#prints false
print(f"19. {nineteen}")

twenty = 3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))
#twenty = true and (not(true or false))
#twenty = true and (not(true))
#prints false
print(f"20. {twenty}")