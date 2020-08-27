
lst1 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

def spinner(lst):                                   # define spinner function dengan parameter lst
    empty_lst1 = []                                 # empty list untuk menampung hasil iterasi nantinya
    empty_lst2 = []                                 # empty list untuk menampung hasil iterasi nantinya
    empty_lst3 = []                                 # empty list untuk menampung hasil iterasi nantinya
    extracted = [j for i in lst for j in i]         # list comprehension disini digunakan untuk mengunpack nested list menjadi 1 list dan ditampung dalam variable extracted
    empty_lst1.extend(extracted[2:: 3])             # function extend disini untuk menambahkan beberapa value dalam satu list empty_lst1 akan ditambahkan 
                                                    # value dari extracted dimulai dari index 2 sampai selesai dengan step 3
    empty_lst2.extend(extracted[1:: 3])             # empty_lst2 akan ditambahkan value dari extracted di mulai dari index 1 sampai selesai dengan step 3
    empty_lst3.extend(extracted[0:: 3])             # empty_lst3 akan ditambahkan value dari extracted di mulai dari index 0 sampai selesai dengan step 3
    return ([empty_lst1, empty_lst2, empty_lst3])   # return function dalam bracket [] digunakan untuk mengubah list menjadi 1 instead of separating it into 3 different lists
print(spinner(lst1))