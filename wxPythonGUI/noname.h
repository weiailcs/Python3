///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/button.h>
#include <wx/statbox.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class LoginFrame
///////////////////////////////////////////////////////////////////////////////
class LoginFrame : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* UserNameText;
		wxTextCtrl* UserName;
		wxStaticText* PassWordText;
		wxTextCtrl* PassWord;
		wxButton* Accept;
		
		// Virtual event handlers, overide them in your derived class
		virtual void submmit( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		LoginFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 300,200 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~LoginFrame();
	
};

#endif //__NONAME_H__
