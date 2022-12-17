################################################################################
##
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
##
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

class Style():

    style_bt_standard = (
        """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """
    )

    style_spinbox_error = (
        """
    QSpinBox{
        background-color: rgb(5, 7, 35);
        border-radius: 5px;
        border: 2px solid #ff0000;
        padding: 5px;
        padding-left: 10px;
    }
    QSpinBox:hover{
	    border: 3px solid #ff0000;
    }
    QSpinBox QAbstractItemView {
        color: rgb(85, 170, 255);	
        background-color: rgb(27, 29, 35);
        padding: 10px;
        selection-background-color: rgb(27, 29, 35);
    }
    
    /*
    rgb(27, 29, 35);
    rgb(13, 9, 59)
    */

    QSpinBox::up-button{
        width: 25px; 
        border-left-width: 3px;
        border-left-color: rgba(39, 44, 54, 150);
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;	
        background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);
        background-position: center;
        background-repeat: no-reperat;
    }

    QSpinBox::up-button:hover{
        background-color: rgb(80, 80, 80)
    }

    QSpinBox::down-button:hover{
        background-color: rgb(80, 80, 80)
    }

    QSpinBox::down-button{
        width: 25px; 
        border-left-width: 3px;
        border-left-color: rgba(39, 44, 54, 150);
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;	
        background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);
        background-position: center;
        background-repeat: no-reperat;
    }
    """)

    style_spinbox_ok = (
            """
        QSpinBox{
            background-color: rgb(5, 7, 35);
            border-radius: 5px;
            border: 2px solid #098c04;
            padding: 5px;
            padding-left: 10px;
        }
        QSpinBox:hover{
            border: 3px solid #098c04;
        }
        QSpinBox QAbstractItemView {
            color: rgb(85, 170, 255);	
            background-color: rgb(27, 29, 35);
            padding: 10px;
            selection-background-color: rgb(27, 29, 35);
        }
        /*
        rgb(27, 29, 35);
        rgb(13, 9, 59)
        */

        QSpinBox::up-button{
            width: 25px; 
            border-left-width: 3px;
            border-left-color: rgba(39, 44, 54, 150);
            border-left-style: solid;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;	
            background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);
            background-position: center;
            background-repeat: no-reperat;
        }

        QSpinBox::up-button:hover{
            background-color: rgb(80, 80, 80)
        }

        QSpinBox::down-button:hover{
            background-color: rgb(80, 80, 80)
        }

        QSpinBox::down-button{
            width: 25px; 
            border-left-width: 3px;
            border-left-color: rgba(39, 44, 54, 150);
            border-left-style: solid;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;	
            background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);
            background-position: center;
            background-repeat: no-reperat;
        }
        """)
    btn_pagechange = ("""
    QPushButton {
	border: 2px solid rgb(56, 170, 72);
	border-radius: 12px;	
	background-color: rgb(63, 152, 90);
}

/* rgb(52, 59, 72)*/
QPushButton:hover {
	background-color: rgb(60, 198, 84);
	border: 2px solid rgb(60, 196, 72);
}
QPushButton:pressed {	
	background-color: rgb(37, 138, 26);
	border: 2px solid rgb(60, 196, 72);
}
    """)
