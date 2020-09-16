--this now works!!!!
powMod :: Integer -> Integer -> Integer -> Integer -> Integer
powMod base exponent modulus return
    | exponent == 0 = return
    | exponent `mod` 2 == 1 = powMod (base * base `mod` modulus) (exponent `div` 2) modulus return
    | otherwise = powMod (base * base `mod` modulus) (exponent `div` 2) modulus (return * base `mod` modulus)