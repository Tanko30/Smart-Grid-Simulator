#!/home/mrpinformcc/anaconda3/bin/python

#####################################################################################################################################################
 #
 # [Author]:(CCI, 2021) BOUBAKAR Zourkalaini
 # [Date]: Fri Sep 10, 2021 
 # [Goal]: Simulate Hybride smart grid
 # [Version]: 2.0 (last version)
 # [Execution]: /bin/python
 #
 ########################################################################################################################################################

#packages 
import math # for the mathematic formula
from tkinter import * # for Graphical interface

############################ Photovoltaic module ###################################################
class PhotovoltaicModule:
    def __init__(self, ws):

        f = ('Times', 14)

        right_frame = Frame(
            ws, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )

        self.lbl0 = Label(
                right_frame, 
                text="Short circuit current (I_sc)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=0, column=0, sticky=W, pady=10)

        self.lbl1 = Label(
                right_frame, 
                text="Idealistic factor (F)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=1, column=0, sticky=W, pady=10)

        self.lbl2 = Label(
                right_frame, 
                text="Open current voltage (V_oc)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=2, column=0, sticky=W, pady=10)


        self.lbl3 = Label(
                right_frame, 
                text="Absolute temperature (T_c)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=3, column=0, sticky=W, pady=10)

        self.lbl4 = Label(
                right_frame, 
                text="Reference temperature (T_r)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=4, column=0, sticky=W, pady=10)
        self.lbl5 = Label(
                right_frame, 
                text="Bang-gap energy of semiconductor (V_g)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=5, column=0, sticky=W, pady=10)

        self.lbl6 = Label(
                right_frame, 
                text="Temperature coef of the short circuit (mu_sc)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=6, column=0, sticky=W, pady=10)

        self.lbl7 = Label(
                right_frame, 
                text="Solar irradiation (G)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=7, column=0, sticky=W, pady=10)


        self.lbl8 = Label(
                right_frame, 
                text="Diode voltage (V_d)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=8, column=0, sticky=W, pady=10)

        self.lbl9 = Label(
                right_frame, 
                text="Parallel resistance (R_p)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=9, column=0, sticky=W, pady=10)

        self.lbl11 = Label(
                right_frame, 
                text="Result (I_pv) = ", 
                bg='#CCCCCC',
                font=f
            ).grid(row=11, column=0, sticky=W, pady=10)


        self.register_I_sc = Entry(
                right_frame, 
                font=f
            )

        self.register_F = Entry(
                right_frame, 
                font=f
            )

        self.register_V_oc = Entry(
                right_frame, 
                font=f
            )


        self.register_T_c = Entry(
                right_frame, 
                font=f
        )

        self.register_T_r = Entry(
                right_frame, 
                font=f
        )

        self.register_V_g = Entry(
                right_frame, 
                font=f
            )

        self.register_mu_sc = Entry(
                right_frame, 
                font=f
            )

        self.register_G = Entry(
                right_frame, 
                font=f
            )



        self.register_V_d = Entry(
                right_frame, 
                font=f
        )

        self.register_R_p = Entry(
                right_frame, 
                font=f
        )

        self.register_Result = Entry(
                right_frame, 
                font=f
        )


        self.register_btn = Button(
                right_frame, 
                width=10, 
                text='Simulate', 
                font=f, 
                relief=SOLID,
                cursor='hand2',
                command=self.photovoltaic_module
        )

        self.register_I_sc.grid(row=0, column=1, pady=10, padx=20)
        self.register_F.grid(row=1, column=1, pady=10, padx=20) 
        self.register_V_oc.grid(row=2, column=1, pady=10, padx=20)
        self.register_T_c.grid(row=3, column=1, pady=10, padx=20)
        self.register_T_r.grid(row=4, column=1, pady=10, padx=20)
        self.register_V_g.grid(row=5, column=1, pady=10, padx=20)
        self.register_mu_sc.grid(row=6, column=1, pady=10, padx=20) 
        self.register_G.grid(row=7, column=1, pady=10, padx=20)
        self.register_V_d.grid(row=8, column=1, pady=10, padx=20)
        self.register_R_p.grid(row=9, column=1, pady=10, padx=20)
        self.register_btn.grid(row=10, column=1, pady=10, padx=20)
        self.register_Result.grid(row=11, column=1, pady=10, padx=20)
        right_frame.pack()

    def photovoltaic_module(self):
        self.register_Result.delete(0, 'end')
        # constant for the photovoltaic module
        e = 1.6 * (10**-19)
        K = 1.38 * (10**-23)

        # input parameters for the photovoltaic module
        I_sc = float(self.register_I_sc.get())
        F = float(self.register_F.get())
        V_oc = float(self.register_V_oc.get())
        T_c = float(self.register_T_c.get())
        T_r = float(self.register_T_r.get())
        V_g = float(self.register_V_g.get())
        mu_sc = float(self.register_mu_sc.get())
        G = float(self.register_G.get())
        V_d = float(self.register_V_d.get())
        R_p = float(self.register_R_p.get())
        
        # formula for the photovoltaic module
        try:
            I_oa = I_sc / (math.exp((e * V_oc) / (K * F * T_c)))
        except OverflowError:
            I_oa = float("inf")
        
        try:
            I_o = I_oa * ((T_c/T_r)**3) * math.exp(((e * V_g) / (K * F)) * (1/T_r - 1/T_c))
        except OverflowError:
            I_o = float("inf")
        
        try:
            I_gc = (mu_sc * (T_c - T_r) + I_sc) * G
        except OverflowError:
            I_gc = float("inf")
        
        try:
            I_pv = I_gc - I_o * (math.exp((e * V_d) / (K * F * T_c)) - 1) - V_d/R_p
        except OverflowError:
            I_pv = float("inf")
        
        # photovoltaic module output
        self.register_Result.insert(END, str(I_pv))

#############################################################################################################

###################### Wind turbine module #################################################
class WindModule:
    def __init__(self, ws):

        f = ('Times', 14)

        right_frame = Frame(
            ws, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )

        self.lbl0 = Label(
                right_frame, 
                text="air density (rho)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=0, column=0, sticky=W, pady=10)

        self.lbl1 = Label(
                right_frame, 
                text="swpet area (A)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=1, column=0, sticky=W, pady=10)

        self.lbl2 = Label(
                right_frame, 
                text="wind speed (v)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=2, column=0, sticky=W, pady=10)


        
        self.lbl11 = Label(
                right_frame, 
                text="Result (power) P = ", 
                bg='#CCCCCC',
                font=f
            ).grid(row=11, column=0, sticky=W, pady=10)


        self.register_rho = Entry(
                right_frame, 
                font=f
            )

        self.register_A = Entry(
                right_frame, 
                font=f
            )

        self.register_v = Entry(
                right_frame, 
                font=f
            )


     
        self.register_Result = Entry(
                right_frame, 
                font=f
        )


        self.register_btn = Button(
                right_frame, 
                width=10, 
                text='Simulate', 
                font=f, 
                relief=SOLID,
                cursor='hand2',
                command=self.wind_module
        )

        self.register_rho.grid(row=0, column=1, pady=10, padx=20)
        self.register_A.grid(row=1, column=1, pady=10, padx=20) 
        self.register_v.grid(row=2, column=1, pady=10, padx=20)
        self.register_btn.grid(row=10, column=1, pady=10, padx=20)
        self.register_Result.grid(row=11, column=1, pady=10, padx=20)
        right_frame.pack()

    def wind_module(self):
        self.register_Result.delete(0, 'end')
        
        # input parameters for the wind module
        rho = float(self.register_rho.get())
        A = float(self.register_A.get())
        v = float(self.register_v.get())
        
        # formula for the wind module
        try:
            P = 0.5 * (rho * A * (v**3))
        except OverflowError:
            P = float("inf")
        
        # wind module output
        self.register_Result.insert(END, str(P))
##########################################################################################################


############################ Hydropower module #######################################
class HydropowerModule:
    def __init__(self, ws):

        f = ('Times', 14)

        right_frame = Frame(
            ws, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )

        self.lbl0 = Label(
                right_frame, 
                text="Dimensionless (n)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=0, column=0, sticky=W, pady=10)

        self.lbl1 = Label(
                right_frame, 
                text="Water density (rho)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=1, column=0, sticky=W, pady=10)

        self.lbl2 = Label(
                right_frame, 
                text="Flow (Q)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=2, column=0, sticky=W, pady=10)
        
        self.lbl3 = Label(
                right_frame, 
                text="Acceleration (g)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=3, column=0, sticky=W, pady=10)

        self.lbl4 = Label(
                right_frame, 
                text="Height difference (h)", 
                bg='#CCCCCC',
                font=f
            ).grid(row=4, column=0, sticky=W, pady=10)


        
        self.lbl11 = Label(
                right_frame, 
                text="Result (power) P = ", 
                bg='#CCCCCC',
                font=f
            ).grid(row=11, column=0, sticky=W, pady=10)


        self.register_n = Entry(
                right_frame, 
                font=f
            )

        self.register_rho = Entry(
                right_frame, 
                font=f
            )

        self.register_Q = Entry(
                right_frame, 
                font=f
            )
         
        self.register_g = Entry(
                right_frame, 
                font=f
            )

        self.register_h = Entry(
                right_frame, 
                font=f
            )


     
        self.register_Result = Entry(
                right_frame, 
                font=f
        )


        self.register_btn = Button(
                right_frame, 
                width=10, 
                text='Simulate', 
                font=f, 
                relief=SOLID,
                cursor='hand2',
                command=self.hydropower_module
        )

        self.register_n.grid(row=0, column=1, pady=10, padx=20)
        self.register_rho.grid(row=1, column=1, pady=10, padx=20) 
        self.register_Q.grid(row=2, column=1, pady=10, padx=20)
        self.register_g.grid(row=3, column=1, pady=10, padx=20) 
        self.register_h.grid(row=4, column=1, pady=10, padx=20)
        self.register_btn.grid(row=10, column=1, pady=10, padx=20)
        self.register_Result.grid(row=11, column=1, pady=10, padx=20)
        right_frame.pack()

    def hydropower_module(self):
        self.register_Result.delete(0, 'end')
        
        # input parameters for the hydropower module
        n = float(self.register_n.get())
        rho = float(self.register_rho.get())
        Q = float(self.register_Q.get())
        g = float(self.register_g.get())
        h = float(self.register_h.get())
        
        # formula for the hydropower module
        try:
            P = n * rho * Q * g * h
        except OverflowError:
            P = float("inf")
        
        # wind module output
        self.register_Result.insert(END, str(P))

#######################################################################

########################## Hybride model ###########################################################
class MyWindow:
    def __init__(self, ws):

        f = ('Times', '18')

        right_frame = Frame(
            ws, 
            bd=10, 
            bg='#CCCCCC',
            relief=RAISED, 
            padx=20, 
            pady=20
            )

        
        self.register_photovoltaic = Button(
                right_frame, 
                width=20, 
                text='Photovoltaic module', 
                font=f, 
                relief=RAISED,
                cursor='hand2',
                command=self.PHOTOVOLTAIC
        )
        
        self.register_wind = Button(
                right_frame, 
                width=20, 
                text='Wind turbine module', 
                font=f, 
                relief=RAISED,
                cursor='hand2',
                command=self.WIND
        )
        
        self.register_hydropower = Button(
                right_frame, 
                width=20, 
                text='Hydropower module', 
                font=f, 
                relief=RAISED,
                cursor='hand2',
                command=self.HYDROPOWER
        )
        
        self.quit = Label(
                right_frame, 
                text="Choose a Module to continue...", 
                bg='#FFFFFF',
                font=f
            ).grid(row=3, column=1, sticky=W, pady=10)


        self.register_photovoltaic.grid(row=0, column=1, pady=20, padx=40)
        self.register_wind.grid(row=1, column=1, pady=20, padx=40) 
        self.register_hydropower.grid(row=2, column=1, pady=20, padx=40)
        right_frame.pack()

    def PHOTOVOLTAIC(self):
        pm = Tk()
        mywin=PhotovoltaicModule(pm)
        pm.title('Photovoltaic module')
        pm.config(bg='#0B5A81')
        pm.mainloop()
    def WIND(self):
        wm = Tk()
        mywin=WindModule(wm)
        wm.title('Wind turbine module')
        wm.config(bg='#0B5A81')
        wm.mainloop()
    def HYDROPOWER(self):
        hm = Tk()
        mywin=HydropowerModule(hm)
        hm.title('Hydropower module')
        hm.config(bg='#0B5A81')
        hm.mainloop()

ws = Tk()
mywin=MyWindow(ws)
ws.title('SMART GRID Simulator')
ws.config(bg='#0B5A81')
ws.mainloop()
######################################################################################################

