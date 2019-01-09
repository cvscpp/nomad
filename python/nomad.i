%module nomad

void NOMAD::display_info ( const NOMAD::Display & out );
void NOMAD::display_version ( const NOMAD::Display & out );
void NOMAD::display_usage ( char* exeName, const NOMAD::Display & out );
void NOMAD::display_usage ( const NOMAD::Display & out );	

class Mads( NOMAD::Parameters & p , NOMAD::Evaluator * ev = NULL );

