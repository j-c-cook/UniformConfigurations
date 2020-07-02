# Jack C. Cook
# 7/1/20

# Creating borehole fields in a line

import Create_Rectangular_Fields as fieldgen


def main():
    # Four boreholes in a line
    # -------- inputs ----------
    BottomY = 1
    LeftX = 4
    SpaceX = 5
    DistanceX = (LeftX - 1) * SpaceX
    # --------------------------

    fgen = fieldgen.Gen_Field.FieldGenerator(BottomY=BottomY, LeftX=LeftX, SpaceX=SpaceX,
                                             DistanceX=DistanceX, Name='line')
    print(fgen.borehole_locations)
    fgen.__display_field__(show_plot=True)
    fgen.__export_field__()


if __name__ == '__main__':
    main()
