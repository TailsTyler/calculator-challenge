import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
// Import the standalone components
import { AppComponent } from './app.component';
import { TokenizerComponent } from './tokenizer/tokenizer.component';

@NgModule({
  // Remove the components from the declarations array
  declarations: [],
  imports: [
    BrowserModule,
    AppRoutingModule,
    // Add standalone components to imports
    AppComponent,
    TokenizerComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
