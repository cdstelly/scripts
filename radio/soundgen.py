#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan  3 21:21:14 2014
##################################################
 
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx
 
class top_block(grc_wxgui.top_block_gui):
 
        def __init__(self):
                grc_wxgui.top_block_gui.__init__(self, title="Top Block")
                _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
                self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))
 
                ##################################################
                # Variables
                ##################################################
                self.samp_rate = samp_rate = 192000
                self.Noise = Noise = 0.01
                self.Loudness = Loudness = 0.7
                self.Frequency = Frequency = 5000
 
                ##################################################
                # Blocks
                ##################################################
                _Noise_sizer = wx.BoxSizer(wx.VERTICAL)
                self._Noise_text_box = forms.text_box(
                        parent=self.GetWin(),
                        sizer=_Noise_sizer,
                        value=self.Noise,
                        callback=self.set_Noise,
                        label="Noise",
                        converter=forms.float_converter(),
                        proportion=0,
                )
                self._Noise_slider = forms.slider(
                        parent=self.GetWin(),
                        sizer=_Noise_sizer,
                        value=self.Noise,
                        callback=self.set_Noise,
                        minimum=0.0,
                        maximum=1,
                        num_steps=1000,
                        style=wx.SL_HORIZONTAL,
                        cast=float,
                        proportion=1,
                )
                self.Add(_Noise_sizer)
                _Loudness_sizer = wx.BoxSizer(wx.VERTICAL)
                self._Loudness_text_box = forms.text_box(
                        parent=self.GetWin(),
                        sizer=_Loudness_sizer,
                        value=self.Loudness,
                        callback=self.set_Loudness,
                        label="Loudness",
                        converter=forms.float_converter(),
                        proportion=0,
                )
                self._Loudness_slider = forms.slider(
                        parent=self.GetWin(),
                        sizer=_Loudness_sizer,
                        value=self.Loudness,
                        callback=self.set_Loudness,
                        minimum=0.0,
                        maximum=1.0,
                        num_steps=1000,
                        style=wx.SL_HORIZONTAL,
                        cast=float,
                        proportion=1,
                )
                self.Add(_Loudness_sizer)
                _Frequency_sizer = wx.BoxSizer(wx.VERTICAL)
                self._Frequency_text_box = forms.text_box(
                        parent=self.GetWin(),
                        sizer=_Frequency_sizer,
                        value=self.Frequency,
                        callback=self.set_Frequency,
                        label="Frequency",
                        converter=forms.int_converter(),
                        proportion=0,
                )
                self._Frequency_slider = forms.slider(
                        parent=self.GetWin(),
                        sizer=_Frequency_sizer,
                        value=self.Frequency,
                        callback=self.set_Frequency,
                        minimum=10,
                        maximum=20000,
                        num_steps=1000,
                        style=wx.SL_HORIZONTAL,
                        cast=int,
                        proportion=1,
                )
                self.Add(_Frequency_sizer)
                self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
                        self.GetWin(),
                        baseband_freq=0,
                        dynamic_range=100,
                        ref_level=0,
                        ref_scale=4.0,
                        sample_rate=samp_rate,
                        fft_size=2048,
                        fft_rate=15,
                        average=False,
                        avg_alpha=0.1,
                        title="Waterfall Plot",
                        size=(900,200),
                )
                self.Add(self.wxgui_waterfallsink2_0.win)
                def wxgui_waterfallsink2_0_callback(x, y):
                        self.set_Frequency(x)
 
                self.wxgui_waterfallsink2_0.set_callback(wxgui_waterfallsink2_0_callback)
                self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
                        self.GetWin(),
                        baseband_freq=0,
                        y_per_div=10,
                        y_divs=10,
                        ref_level=0,
                        ref_scale=4.0,
                        sample_rate=samp_rate,
                        fft_size=2048,
                        fft_rate=15,
                        average=True,
                        avg_alpha=0.1,
                        title="FFT Plot",
                        peak_hold=True,
                )
                self.Add(self.wxgui_fftsink2_0.win)
                self.gr_sig_source_x_2 = gr.sig_source_c(samp_rate, gr.GR_SIN_WAVE, Frequency, Loudness, 0)
                self.gr_noise_source_x_0 = gr.noise_source_c(gr.GR_GAUSSIAN, Noise, 0)
                self.gr_complex_to_real_0 = gr.complex_to_real(1)
                self.gr_add_xx_1 = gr.add_vcc(1)
                self.audio_sink_0 = audio.sink(samp_rate, "", True)
 
                ##################################################
                # Connections
                ##################################################
                self.connect((self.gr_complex_to_real_0, 0), (self.audio_sink_0, 0))
                self.connect((self.gr_noise_source_x_0, 0), (self.gr_add_xx_1, 0))
                self.connect((self.gr_sig_source_x_2, 0), (self.gr_add_xx_1, 1))
                self.connect((self.gr_add_xx_1, 0), (self.gr_complex_to_real_0, 0))
                self.connect((self.gr_add_xx_1, 0), (self.wxgui_waterfallsink2_0, 0))
                self.connect((self.gr_add_xx_1, 0), (self.wxgui_fftsink2_0, 0))
 
        def get_samp_rate(self):
                return self.samp_rate
 
        def set_samp_rate(self, samp_rate):
                self.samp_rate = samp_rate
                self.gr_sig_source_x_2.set_sampling_freq(self.samp_rate)
                self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
                self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
 
        def get_Noise(self):
                return self.Noise
 
        def set_Noise(self, Noise):
                self.Noise = Noise
                self.gr_noise_source_x_0.set_amplitude(self.Noise)
                self._Noise_slider.set_value(self.Noise)
                self._Noise_text_box.set_value(self.Noise)
 
        def get_Loudness(self):
                return self.Loudness
 
        def set_Loudness(self, Loudness):
                self.Loudness = Loudness
                self._Loudness_slider.set_value(self.Loudness)
                self._Loudness_text_box.set_value(self.Loudness)
                self.gr_sig_source_x_2.set_amplitude(self.Loudness)
 
        def get_Frequency(self):
                return self.Frequency
 
        def set_Frequency(self, Frequency):
                self.Frequency = Frequency
                self._Frequency_slider.set_value(self.Frequency)
                self._Frequency_text_box.set_value(self.Frequency)
                self.gr_sig_source_x_2.set_frequency(self.Frequency)
 
if __name__ == '__main__':
        parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
        (options, args) = parser.parse_args()
        tb = top_block()
        tb.Run(True)
