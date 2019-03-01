from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f = open(fname,"r")
    s = f.read()
    l = s.split()
    i=0
    while i < len(l):
		if l[i] == 'line':
			add_edge(points,int(l[i+1]),int(l[i+2]),int(l[i+3]),int(l[i+4]),int(l[i+5]),int(l[i+6]))
			i+=7
		if l[i] == 'ident':
			ident(transform)
			i+=1
		if l[i] == 'scale':
			scale = make_scale(int(l[i+1]),int(l[i+2]),int(l[i+3]))
			matrix_mult(scale,transform)
			i+=4
		if l[i] == 'move':
			translate = make_translate(int(l[i+1]),int(l[i+2]),int(l[i+3]))
			matrix_mult(translate,transform)
			i+=4
		if l[i] == 'rotate':
			if(l[i+1]=='x'):
				rotX = make_rotX(int(l[i+2]))
				matrix_mult(rotX,transform)
			if(l[i+1]=='y'):
				rotY = make_rotY(int(l[i+2]))
				matrix_mult(rotY,transform)
			if(l[i+1]=='z'):
				rotZ = make_rotZ(int(l[i+2]))
				matrix_mult(rotZ,transform)
			i+=3
		if l[i] == 'apply':
			matrix_mult(transform,points)
			i+=1
		if l[i] == 'display':
			clear_screen(screen)
			draw_lines(points,screen,color)
			display(screen)
			i+=1
		if l[i] == 'save':
			clear_screen(screen)
			draw_lines(points,screen,color)
			display(screen)
			save_extension(screen, int(l[i+1]))
			i+=2
		if l[i] == 'quit':
			f.close()
    		pass
