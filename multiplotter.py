# -*- coding: utf-8 -*-
"""
Created on Sat May 19 02:26:29 2012

@author: Tillsten
"""

from numpy import linspace, random, zeros, arange, cumprod
import numpy as np
import time


# ETS imports (non-chaco)
from enable.component_editor import ComponentEditor
from enable.api import BaseTool
from traits.api import HasTraits, Instance, Int, List, Str, Array
from traitsui.api import Item, View

# Chaco imports
from chaco.api import ArrayPlotData, Plot
from chaco.tools.api import PanTool, ZoomTool, RangeSelection, \
        RangeSelectionOverlay, LegendTool



from chaco.example_support import COLOR_PALETTE

from chaco.default_colors import palette11 as COLOR_PALETTE
#from enthought.chaco.example_support import COLOR_PALETTE
COLOR_PALETTE=['blue','green','red','cyan','yellow','pink']

class MultiPlotter(HasTraits):
    plot=Instance(Plot)
    xaxis=Array
    ytemp=Array
    ydata=List(Array)
    pd=Instance(ArrayPlotData)
   
    xlabel=Str('')
    ylabel=Str('')    
    
    def _pd_default(self):
        pd=ArrayPlotData(x=self.xaxis,ytemp=self.ytemp)        
        return pd
        
    def _xlabel_changed(self,new):        
        self.plot.x_axis.title=new
        
    def _ylabel_changed(self,new):        
        self.plot.y_axis.title=new
     
    
    def _plot_default(self):
        plot=Plot(self.pd)        
        plot.plot(('x','ytemp'),name='cursor')
        plot.legend.visible=True
        plot.tools.append(PanTool(plot, drag_button='right'))        
        zoom = ZoomTool(component=plot, tool_mode="box", always_on=True)
        plot.overlays.append(zoom)          
        return plot
    
    def _ytemp_changed(self):
        self.pd.set_data('ytemp',self.ytemp)   

    def delete_ydata(self):
        self.ydata=[]        
        l=[]
        for i in self.plot.plots:
           l.append(i)
        for i in l:
            self.plot.delplot(i)
        self.plot.plot(('x','ytemp'),name='cursor')
        
    def add_ydata(self,name, y):
        self.ydata.append(y)
        self.pd.set_data(name,y)
        c=COLOR_PALETTE[(len(self.ydata)-1)%len(COLOR_PALETTE)]
        self.plot.plot(('x',name),name=name,color=c,line_width=3.)
        self.plot.request_redraw()

        

    traits_view=View(Item('plot',editor=ComponentEditor(size=(400,400))))


if __name__=='__main__':
    x=np.linspace(0,10,100)
    y=np.sin(x)         
    mlp=MultiPlotter(xaxis=x)
    mlp.add_ydata('sin',y)
    
    mlp.xlabel='dsfj'    
    #mlp.delete_ydata()
    mlp.configure_traits()
    
  