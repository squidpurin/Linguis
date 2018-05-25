class Mapper:
    def __init__(self):
        self.mapping = {'p':'vls_lbl_psv.wav',
                        'b':'vcd_lbl_psv.wav',
                        't':'vls_alv_psv.wav',
                        'd':'vcd_alv_psv.wav',
                        'c':'vls_plt_psv.wav',
                        'ɟ':'vcd_plt_psv.wav',
                        'k':'vls_vlr_psv.wav',
                        'ɡ':'vcd_vlr_psv.wav',
                        'q':'vls_uvl_psv.wav',
                        'ɢ':'vcd_uvl_psv.wav',
                        'ʔ':'vls_glt_psv.wav',
                        'm':'vcd_blb_nsl.wav',
                        'ɱ':'vcd_lbd_nsl.wav',
                        'n':'vcd_alv_nsl.wav',
                        'ɳ':'vcd_ret_nsl.wav',
                        'ŋ':'vcd_vlr_nsl.wav',
                        'ɴ':'vcd_uvl_nsl.wav',
                        'ʙ':'vcd_blb_trl.wav',
                        'r':'vcd_alv_trl.wav',
                        'ʀ':'vcd_uvl_trl.wav',
                        'ⱱ':'vcd_lbd_tap.wav',
                        'ɾ':'vcd_alv_tap.wav',
                        'ɽ':'vcd_ret_tap.wav',
                        'ɸ':'vls_blb_fri.wav',
                        'β':'vcd_blb_fri.wav',
                        'f':'vls_lbd_fri.wav',
                        'v':'vcd_lbd_fri.wav',
                        'θ':'vls_dtl_fri.wav',
                        'ð':'vcd_dtl_fri.wav',
                        's':'vls_alv_fri.wav',
                        'z':'vcd_alv_fri.wav',
                        'ʃ':'vls_pav_fri.wav',
                        'ʒ':'vcd_pav_fri.wav',
                        'ʂ':'vls_ret_fri.wav',
                        'ʐ':'vcd_ret_fri.wav',
                        'ç':'vls_plt_fri.wav',
                        'ʝ':'vcd_plt_fri.wav',
                        'x':'vls_vlr_fri.wav',
                        'ɣ':'vcd_vlr_fri.wav',
                        'χ':'vls_uvl_fri.wav',
                        'ʁ':'vcd_uvl_fri.wav',
                        'h':'vls_glt_fri.wav',
                        'ʕ':'vcd_pha_fri.wav',
                        'ħ':'vls_pha_fri.wav',
                        'ɦ':'vcd_glt_fri.wav',
                        'ɬ':'vls_alv_lfr.wav',
                        'ɮ':'vcd_alv_lfr.wav',
                        'ʋ':'vcd_lbd_apx.wav',
                        'ɹ':'vcd_alv_apx.wav',
                        'j':'vcd_plt_apx.wav',
                        'ɰ':'vcd_vlr_apx.wav',
                        'l':'vcd_alv_lap.wav',
                        'ɭ':'vcd_ret_lap.wav',
                        'ʎ':'vcd_plt_lap.wav',
                        'ʟ':'vcd_vlr_lap.wav',
                        'ʘ':'vls_blb_clk.wav',
                        '|':'vls_dtl_clk.wav',
                        'ǂ':'vls_pav_clk.wav',
                        'ǁ':'vls_avl_clk.wav', #alveolo-lateral
                        '!':'vls_alv_clk.wav',
                        'ɓ':'vcd_blb_imp.wav',
                        'ɗ':'vcd_alv_imp.wav',
                        'ɠ':'vcd_vlr_imp.wav',
                        'ʄ':'vcd_plt_imp.wav',
                        'ʛ':'vcd_uvl_imp.wav',
                        'p\'':'vls_blb_eje.wav',
                        't\'':'vls_alv_eje.wav',
                        'k\'':'vls_vlr_eje.wav',
                        's\'':'vls_alv_sej.wav', #sibilant ejective
                        'ʍ':'vls_lbv_apx.wav', #labio-velar
                        'w':'vcd_lbv_apx.wav',
                        'ɥ':'vcd_lpl_apx.wav', #labio-palatal
                        'ʜ':'vls_epi_trl.wav',
                        'ʢ':'vcd_epi_trl.wav',
                        'ʡ':'vcd_epi_psv.wav',
                        'ɕ':'vls_avp_fri.wav', #alveolo-palatal
                        'ʑ':'vcd_avp_fri.wav',
                        'ɺ':'vcd_avl_tap.wav',
                        'ɧ':'vls_vpa_fri.wav', #velo-postalveolar
                        'k͡p':'vls_vbl_psv.wav', #velo-bilabial
                        't͡s':'vls_alv_afr.wav', #affricate
                        'i':'cl_fr_u.wav',
                        'y':'cl_fr_r.wav',
                        'ɨ':'cl_ce_u.wav',
                        'ʉ':'cl_ce_r.wav',
                        'ɯ':'cl_bk_u.wav',
                        'u':'cl_bk_r.wav',
                        'ɪ':'nc_nf_u.wav',
                        'ʏ':'nc_nf_r.wav',
                        'ʊ':'nc_nb_r.wav',
                        'e':'cm_fr_u.wav',
                        'ø':'cm_fr_r.wav',
                        'ɘ':'cm_ce_u.wav',
                        'ɵ':'cm_ce_r.wav',
                        'ɤ':'cm_bk_u.wav',
                        'o':'cm_bk_r.wav',
                        'ə':'mi_ce_u.wav',
                        'ɛ':'om_fr_u.wav',
                        'œ':'om_fr_r.wav',
                        'ɜ':'om_ce_u.wav',
                        'ɞ':'om_ce_r.wav',
                        'ʌ':'om_bk_u.wav',
                        'ɔ':'om_bk_r.wav',
                        'æ':'no_fr_u.wav',
                        'ɐ':'no_ce_u.wav',
                        'a':'op_fr_u.wav',
                        'ɶ':'op_fr_r.wav',
                        'ɑ':'op_bk_u.wav',
                        'ɒ':'op_bk_r.wav',
                        'ʰ':'aspirant.wav',
                        '' :'null.wav',
                        ' ':'null.wav'}
        def addMapper(self, key, sound_file):
            if key not in self.mapping:
                self.mapping[key] = [sound_file]

import copy, os, pyaudio, wave
from pydub import AudioSegment

class Text2Speech:
    def __init__(self):
        self.mapper = Mapper()

    def decode(self, text):
        text = list(text)
        for i in range(len(text) - 2):
            if text[i+1] == '͡':
                text[i] = ''.join(text[i:i+3])
                text[i+1] = ''
                text[i+2] = ''
            elif text[i+1] == '\'':
                text[i] = ''.join(text[i:i+2])
                text[i+1] = ''
            elif text[i+1] == 'ː':
                text[i+1] = copy.deepcopy(text[i])
        if text[-1] == '\'':
            text[-2] = text[-2] + "\'"
            text[-1] = ''
        text = list(filter(lambda a: a != '', text))
        for i in range(len(text)):
            text[i] = self.mapper.mapping[text[i]]
        return text

    def decodeNoMap(self, text):
        text = list(text)
        for i in range(len(text) - 2):
            if text[i+1] == '͡':
                text[i] = ''.join(text[i:i+3])
                text[i+1] = ''
                text[i+2] = ''
            elif text[i+1] == '\'':
                text[i] = ''.join(text[i:i+2])
                text[i+1] = ''
            elif text[i+1] == 'ː':
                text[i+1] = copy.deepcopy(text[i])
        if text[-1] == '\'':
            text[-2] = text[-2] + "\'"
            text[-1] = ''
        text = list(filter(lambda a: a != '', text))
        return text  

    def wav_combine(self, seq, fn = None):
        sequence = AudioSegment.from_wav("./shortened_sound/null.wav")
        for phoneme in seq:
            sequence += AudioSegment.from_wav("./shortened_sound/" + phoneme)
        if fn == None:
            sequence.export("sequence.wav", format="wav")
            self.play_audio("sequence.wav")
            os.remove("sequence.wav")
        else:
            sequence.export(fn, format="wav")

    def play_audio(self, fn):
        chunk = 1024
        try:
            f = wave.open(fn,"rb")
            p = pyaudio.PyAudio()
            stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)
            data = f.readframes(chunk)  
            while data:  
                stream.write(data)  
                data = f.readframes(chunk)  
            stream.stop_stream()  
            stream.close()  
            p.terminate()
        except:
            print(fn + "is not found")
            
