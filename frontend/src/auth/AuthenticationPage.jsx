import "react"
import {SingIn, SignUp, SignedIn, SignedOut} from '@clerk/clerk-react'

export function AuthenticationPage() {
    return <div className="auth-container">
        <SignedOut>
        // If SignedOut, display this
            <SignIn routing="path" path="/sign-in" />
            <SignUp routing="path" path="/sign-up" />
            <p>Welcome to the Genki Practice App! Please sign in or sign up to continue.</p>
            <p>If you don't have an account, please sign up first.</p>
        </SignedOut>
        <SignedIn>
        // If SignedIn, display this
        </SignedIn>
    </div>
}