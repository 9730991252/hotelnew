def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        processed_combinations = set()

        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            combination = (th_id, tbn)

            if combination not in processed_combinations:
                one_table = Table.objects.filter(hotel_id=th_id, table_number=tbn).first()
                if one_table:
                    send_table.append(one_table)
                    processed_combinations.add(combination)
                    print(one_table)

        data = {
            'all_table': send_table,
        }
        return render(request, 'order/hotel_dashboard.html', data)
    
    else:
        return redirect('hotel_login')
    









def hotel_dashboard (request):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hm)
        t=Cart.objects.filter(hotel_id=h.id)
        for cart_item in t:
                    total += (cart_item.price*cart_item.qty)
        context={
            'h':h,
            't':t,
            'total':total,
        }
        return render(request,'order/hotel_dashboard.html',context=context)
    else:
        return redirect('hotel_login')






def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            send_table.extend(Table.objects.filter(hotel_id=th_id, table_number=tbn))
            print(send_table)

        data = {
            'all_table': send_table,
        }
        return render(request, 'order/hotel_dashboard.html', data)
    
    else:
        return redirect('hotel_login')
    























    

def employee(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        e=Employee.objects.filter(hotel_id=h.id)
        context={
            'h':h,
            'e':e
        }
        if request.method == "POST":
            if "Add" in request.POST:
                hotel_id=request.POST.get('hotel_id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                department=request.POST.get('department')
                Employee.objects.create(
                    hotel_id=hotel_id,
                    employee_name=employee_name,
                    employee_address=employee_address,
                    employee_mobile=employee_mobile,
                    pin=pin,
                    department=department,
                    added_by=h.hotel_name
                )
                messages.success(request,"Employee Added Succesfully")        
                
            elif "Edit" in request.POST:
                hotel_id=request.POST.get('hotel_id')
                id=request.POST.get('id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                department=request.POST.get('department')
                #print(id)
                Employee(
                    hotel_id=hotel_id,
                    id=id,
                    employee_name=employee_name,
                    employee_address=employee_address,
                    employee_mobile=employee_mobile,
                    pin=pin,
                    department=department,
                    added_by=h.hotel_name,
                ).save()
                messages.success(request,"Employee Edit Succesfully") 
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Employee.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Employee.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Employee.objects.get(id=id)
                ac.status='1'
                ac.save()                                   
            
        return render(request,'order/employee.html',context=context)
    else:
        return redirect('hotel_login')
