import "react"
import {SignIn, SignUp, SignedIn, SignedOut} from '@clerk/clerk-react'

export function AuthenticationPage() {
    return <div className="auth-container">
        <SignedOut>
        {/* If SignedOut, display this */}
            <SignIn routing="path" path="/sign-in"/>
            <SignUp routing="path" path="/sign-up"/>
        </SignedOut>
        <SignedIn>
            <div className="redirect-message">
                <p>You are already signed in. Redirecting you to the main page...</p>
            </div>
        </SignedIn>
    </div>
}