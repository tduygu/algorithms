months = {
    1: 'Ocak',
    2: 'Şubat',
    3: 'Mart',
    4: 'Nisan',
    5: 'Mayıs',
    6: 'Haziran',
    7: None
}

print(9 in months)
print('Ocak' in months.values())
print('ten' not in months)
print(len(months))

acc = {
    True : 'zero',
    'a': 'zero',
    1: 'true',
    False: 0
}
print(all(acc))
print(any(acc))

print(sorted(months))
