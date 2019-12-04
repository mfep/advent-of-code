#include <array>
#include <cassert>
#include <cmath>
#include <iostream>

namespace
{

constexpr int InputStart = 353096;
constexpr int InputEnd = 843212;
constexpr int NumDigits = 6;

std::array<int, NumDigits> getDigits(int val)
{
    std::array<int, NumDigits> ret{};
    for (size_t i = 0; i < NumDigits; i++)
    {
        const int decimal = int(pow(10, NumDigits - 1 - i));
        const int digit = val / decimal;
        val -= digit * decimal;
        ret[i] = digit;
    }
    return ret;
}

bool isValid1(const int val)
{
    const auto digits = getDigits(val);
    bool hasPair{ false };
    for (size_t i = 0; i < NumDigits - 1; i++)
    {
        if (digits[i] > digits[i + 1])
            return false;
        hasPair |= digits[i] == digits[i + 1];
    }
    return hasPair;
}

bool isValid2(const int val)
{
    const auto digits = getDigits(val);
    for (size_t i = 0; i < NumDigits - 1; i++)
        if (digits[i] > digits[i + 1])
            return false;

    bool hasPair{ false };
    int prev{ -1 };
    int length{ 1 };
    for (int current : digits)
    {
        if (current == prev)
        {
            ++length;
        }
        else
        {
            hasPair |= length == 2;
            length = 1;
        }
        prev = current;
    }
    hasPair |= length == 2;
    return hasPair;
}

}

int main()
{
    assert(isValid1(111111));
    assert(!isValid1(223450));
    assert(!isValid1(123789));
    assert(isValid1(122789));

    assert(isValid2(112233));
    assert(!isValid2(123444));
    assert(isValid2(111122));

    int count1{}, count2{};
    for (int current = InputStart; current <= InputEnd; ++current)
    {
        count1 += isValid1(current) ? 1 : 0;
        count2 += isValid2(current) ? 1 : 0;
    }
    std::cout << "Part One: " << count1 << "\nPart Two: " << count2 << '\n';

}
