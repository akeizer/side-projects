#!/usr/bin/python
from gi.repository import Gtk, Gio

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Idea Gen Farm")

        self.set_border_width(10)
        self.set_default_size(500, 200)

        self.hb = Gtk.HeaderBar()
        self.hb.props_show_close_button = True   
        self.hb.props.title = "Idea Gen"
        self.set_titlebar(self.hb)

        self.backbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.backbox.get_style_context(), "linked")

        self.back_button = Gtk.Button()
        self.back_button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        self.back_button.connect("clicked", self.back_clicked)
        self.backbox.add(self.back_button)

        self.hb.pack_start(self.backbox)

        self.backbox.hide()

        # button = Gtk.Button()
        # icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        # image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        # button.add(image)
        # hb.pack_end(button)

        self.main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 7)
        ####################Main - Page##################################
        self.tbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.bbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)

        self.main_box.pack_start(self.tbox, True, True, 0)
        self.main_box.pack_start(self.bbox, True, True, 0)

        self.top_label = Gtk.Label()
        self.top_label.set_markup("<big><big>Welcome to The Idea Generation Tool!</big></big>")
        self.top_label.set_justify(Gtk.Justification.CENTER)
        self.tbox.pack_start(self.top_label, True, True, 0)

        self.button1 = Gtk.Button("Software Side Project Idea!")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.bbox.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button("Book Topic!")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.bbox.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button("I Don't Need an Idea!")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.bbox.pack_end(self.button3, True, True, 0)

        self.button4 = Gtk.Button("View My Fav Ideas!")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.bbox.pack_end(self.button4, True, True, 0)

        self.button5 = Gtk.Button("Add My Own Idea!")
        self.button5.connect("clicked", self.on_button5_clicked)
        self.bbox.pack_start(self.button5, True, True, 0)

        ####################End of Main Page##############################

        ####################First Page############################
        self.first_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 15)
        self.main_box.pack_start(self.first_box, True, True, 0)
        
        self.first_title_label = Gtk.Label()
        self.first_title_label.set_markup("<big>Presenting Your Software Idea!</big>")
        self.first_title_label.set_justify(Gtk.Justification.CENTER)
        self.first_box.pack_start(self.first_title_label, True, True, 0)

        #####################END OF FIRST PAGE##########################

        
        self.add(self.main_box)

       # self.clear_software()


    def clear_main(self):
        self.tbox.hide()
        self.bbox.hide()
   
    def show_main(self):
        self.current = "main"
        self.tbox.show()
        self.bbox.show()

    def clear_software(self):
        self.first_box.hide();
        self.backbox.hide();

    def show_software(self):
        self.backbox.show()
        self.first_box.show();

    def on_button1_clicked(self, widget):
        f = open('list')
        for word in f.read().split():
            print(word)
        #print("Hello")
        f.close()
        self.clear_main()
        self.current = "Software"
        self.show_software();

    def on_button2_clicked(self, widget):
        print("Goodbye")
        self.clear_main()
        self.current = "Book"
        

    def on_button3_clicked(self, widget):
        print("Goodbye")
        Gtk.main_quit()

    def on_button4_clicked(self, widget):
        f = open('fav_ideas')
        for word in f.readlines():
            print(word)
        f.close()
        self.current = "Fav_List"

    def on_button5_clicked(self, widget):
        f = open('fav_ideas', 'a')
        f.write("Something, For now\n")
        f.close()
        self.show_main()
        self.current = "Insert Fav"

    def back_clicked(self, widget):
        if(self.current == "Software"):
            self.clear_software()
            self.show_main(); 

    def hide_all_but_main(self):
        self.clear_software()

    
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.hide_all_but_main()
Gtk.main()


