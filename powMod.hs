--this doesn't work
powMod :: Integer -> Integer -> Integer -> Integer -> Integer
powMod base exponent modulus return
    | exponent == 0 = return
    | exponent `mod` 2 == 0 = powMod (base * base `mod` modulus) (exponent `div` 2) modulus return
    | otherwise = powMod (base * base `mod` modulus) (exponent `div` 2) modulus (return * base `mod` modulus)
--but this does
modExp :: Integer -> Integer -> Integer -> Integer
modExp  x y n = mod (x^(mod y (n-1))) (n)
--and this one too
powm :: Integer -> Integer -> Integer -> Integer -> Integer
powm b 0 m r = r
powm b e m r
  | e `mod` 2 == 1 = powm (b * b `mod` m) (e `div` 2) m (r * b `mod` m)
powm b e m r = powm (b * b `mod` m) (e `div` 2) m r