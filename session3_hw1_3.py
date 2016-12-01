from turtle import *

#Ve hình vuông, truong hop cu the:

so_canh_hinh_vuong = int(input("hình vuông co may canh?"))
print ("Hình vuông có {0} canh".format(so_canh_hinh_vuong))

mot_goc_cua_hinh_vuong_bang_bao_nhieu_do = 360 / so_canh_hinh_vuong

for i in range (so_canh_hinh_vuong):
    forward(100)
    lt(mot_goc_cua_hinh_vuong_bang_bao_nhieu_do)

#Ve ngu giác, truong hop cu the:
    
so_canh_hinh_ngu_giac = int(input("hình ngu giác có may canh?"))
print ("Hình ngu giác có {0} canh".format(so_canh_hinh_ngu_giac))

mot_goc_cua_hinh_ngu_giac_bang_bao_nhieu_do = 360 / so_canh_hinh_ngu_giac

for i in range (so_canh_hinh_ngu_giac):
    forward(100)
    lt(mot_goc_cua_hinh_ngu_giac_bang_bao_nhieu_do)


#truong hop tông quát:

hình_n_giác = \
    [4,
     5,
     6,
     7,
     9,
     10]

for socanh in hình_n_giác:

    so_do_goc = 360/socanh

    for i in range(0,socanh):

        if i % 2 == 0:
            color("red")
        if i % 2 == 1:
            color("blue")
        forward(100)
        lt(so_do_goc)


