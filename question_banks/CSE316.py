
questions = {
    "TheWorldWideWeb": {
        "Name some web standards managed by an international consortium.": "HTML, Javascript, JSON, HTTP",
        "Which one of the following is a built-in mechanism Web applications can use to store user-related data inside the browser even after the user closes the browser?": "cookies",
        "From the perspective of the web browser, what is the data structure/format of local storage?": "Hash Map",
        """
        Given the following incomplete HTML, fill in the missing elements so it correctly displays a title in the browser tab and a visible heading on the page:
        <!DOCTYPE html>
        <html>
        __________
        <title>My Webpage</title>
        __________
        __________
        <h1>Welcome to My Webpage</h1>
        __________
        </html>
        """: "<head> and <body> elements",
        "Where should you place <script> tags in an HTML file and why?": "Just before </body> so HTML loads first",
        "What is the purpose of the <!DOCTYPE html> declaration?": "To force standards-compliant HTML5 rendering",
        "What is the difference between selecting an element, class, and ID?": "Elements select all tags, classes can be reused, IDs are unique",
        "Name any three valid values of the position property shown in our slides": "static, relative, absolute, fixed, sticky",
        """
        HTML:
        <div class =\"box\">Hello</div>
        CSS:
        .box {
        width: 200px; padding: 10px 20px; border: 2px solid; margin: 5px; box-sizing: content-box;
        }
        What is the element's total rendered width (excluding margin)?
        """: "244px",
    },
    "JavaScript": {
        "Does the filter() method modify the original array? Explain.": "No because it is not in-place",
        "What is the return type of slice and splice?": "Array",
        """
        For the following JavaScript code, assume it runs without failing. What output would be produced?
        class Song {
            constructor(initArtist, initTitle) {
                this.artist = initArtist;
                this.title = initTitle;
            }
            display() {
                console.log(this.title + " by " + this.artist);
            }
        }
        let song1 = new Song("Owner of a Lonely Heart", "Yes");
        let song2 = new Song("Thriller", "Michael Jackson");
        Object.getPrototypeOf(song2).display = function() {
            console.log(this.title + " (" + this.artist + ")");
        }
        song1.display();
        song2.display();
        """: "Yes (Owner of a Lonely Heart) Michael Jackson (Thriller)",
        """
        For the following JavaScript code, assume it runs without failing. What output would be produced?
        class Song {
            constructor(initArtist, initTitle) {
                this.artist = initArtist;
                this.title = initTitle;
            }
            display() {
                console.log(this.title + " by " + this.artist);
            }
        }
        let song1 = new Song("Yes", "Owner of a Lonely Heart");
        let song2 = new Song("Michael Jackson", "Thriller");
        song2.display = function() {
            console.log(this.title + " (" + this.artist + ")");
        }
        song1.display();
        song2.display();
        """: "Owner of a Lonely Heart by Yes Thriller (Michael Jackson)",
        "In JavaScript, what type does Array.prototype.slice return?": "Array",
        "What JavaScript function takes a String formatted like a JavaScript object with properties and values and converts it into a JavaScript Object, returning that object?": "JSON.parse",
        """
        What would print out from running the following code?
        let names = [];
        names[3] = "John";
        names[0] = "Paul";
        names[1] = "George";
        console.log(names.length);
        """: "4",
        """
        How many Beatles would the code below tell us there are?
        let INSTRUMENTS = {
            BASS: "BASS",
            DRUMS: "DRUMMER",
            LEAD_GUITAR: "LEAD_GUITAR",
            RHYTHM_GUITAR: "RHYTHM_GUITAR"
        };
        let beatles = new Array();
        beatles[INSTRUMENTS.BASS] = "Paul";
        beatles[INSTRUMENTS.DRUMS] = "Richard";
        beatles[INSTRUMENTS.LEAD_GUITAR] = "George";
        beatles[INSTRUMENTS.RHYTHM_GUITAR] = "John";
        console.log("There are " + beatles.length + " beatles");
        """: "0",
        """
        let INSTRUMENTS = {
        BASS: "BASS",
        DRUMS: "DRUMMER",
        LEAD_GUITAR: "LEAD_GUITAR",
        RHYTHM_GUITAR: "RHYTHM_GUITAR"
        };
        let beatles = new Array();
        beatles[INSTRUMENTS.BASS] = "Paul";
        beatles[INSTRUMENTS.DRUMS] = "Richard";
        beatles[INSTRUMENTS.LEAD_GUITAR] = "George";
        beatles[INSTRUMENTS.RHYTHM_GUITAR] = "John";
        console.log("There are " + beatles.length + " beatles");
        Assuming it follows the code in the previous question, what would print from running the code below?
        """: "[ 'BASS', 'DRUMMER', 'LEAD_GUITAR', 'RHYTHM_GUITAR' ]",
        "When calling the map function on a JavaScript array of Strings, what type of argument would be sent to your provided callback function?": "String",
        "When calling the filter function on a JavaScript array of Strings, what type is returned by your provided callback function?": "Boolean",
        "What Node function is not available for use in native ECMA Script as executed by a Web browser?": "require",
        "JavaScript is not a strongly typed language. Which one of the following is not a standard variable type?": "int",
        "Explain what happens when you try to access a property that doesn't exist on a JavaScript object": "undefined after prototype lookup",
        """
        What's wrong with this object creation and how would you fix it?
        function Person(name){
        this,name=name;
        }

        const john = Person(\"John\");
        console.log(john.name);
        """: "Missing new keyword and incorrect assignment",
        """
        Predict the output of this array method chain:
        const numbers = [1,2,3,4,5];
        const result = numbers
        .map(n => n * 2)
        .filter(n => n > 5)
        .reduce((sum, n) => sum + n, 0);
        console.log(result);
        """: "24",
        "What is the fundamental difference between a sequential array and an associative array in JavaScript, particularly regarding the length property?": "Associative arrays do not update length",
        "What property of a constructor function holds the methods and properties that will be shared by all instances created with that constructor?": "prototype",

    },
    "ReactiveProgramming": {
        "What is prop drilling and why is it considered a design problem?": "Prop drilling is passing props through unnecessary components to reach a deep child, and it is a problem because it makes code harder to maintain and reuse. Its because of react component hierarchy",
        "If we were to call myFunction().then() what would we assume about myFunction?": "It returns a promise",
        "What is the DOM that react uses?": "Virtual DOM",
        "How is data flowed from the virtual DOM to the DOM?": "React Fiber compares the previous virtual DOM with the new virtual DOM, determines the minimal set of changes, and applies those changes to the real DOM.",
        "What does render return?":"a JSX component with a single HTML elemet",
        "What must you do to create custom React class-based components?":"Extend React.Component then Override render",
        "How is state actually updated when setState is called?":"setState schedules a state update that may be batched, causing React to re-render the component.",
        "is splice in-place or not":"in-place",
        "Is slice in-place or not": "It is not in-place",
        "What does an in-place function mean? What if its not in place?": "In-place functions mutate the actual variable (usually array) being passed in. If something is not in-place instead it returns a completely new collection, leaving the original untouched.",
        "Name the 3 of the common react.component lifecycle methods":"""
        componentWillMount
        componentDidMount
        componentWillRecieveProps
        shouldComponentUpdate
        componentWillUpdate
        componentDidUpdate
        componentWillUnmount
        """,
        "Which lifecycle method is executed before rendering on both the server and client side?": "componentWillMount",
        "Which lifecycle method runs after the first render only on the client side and is commonly used for AJAX requests, DOM interaction, or timers?": "componentDidMount",
        "Which lifecycle method is invoked when a component receives new props before a re-render occurs?": "componentWillReceiveProps",
        "Which lifecycle method determines whether a component should re-render by returning true or false?": "shouldComponentUpdate",
        "Which lifecycle method is called immediately before a component re-renders?": "componentWillUpdate",
        "Which lifecycle method is called immediately after a component has re-rendered?": "componentDidUpdate",
        "Which lifecycle method is called when a component is removed from the DOM and used for cleanup?": "componentWillUnmount"

    },
    "ReactiveStateManagement": {
        "To what code unit did we delegate the job of determining the next state of our data store based on the previous state and the type of action being performed?": "Reducer",
        "In React, how do you create what you called ephemeral state variables?": "using useState inside a functional component",
        "In HW3, what did you send to low-level components via React Context?": "Store",
        "In HW 3, functions in what object would directly call our transactions' executeDo and executeUndo functions?": "tps",
        "What is the React method that you must always use to update a component's state in class-based components, instead of modifying state directly?": "setState",
        r"""
        Consider the following code:
        export default class NameList extends React.Component {
        constructor(props){
            super(props);
            this.state = {number:0}
        }
        handleClick = () => {
            this.setState({number: this.state.number+1})
            this.props.addNumCallback(this.state.number);
        }
        render() {
            return(
                <ul>{this.props.names.map((name, index) => {
                    return <li key={index} onClick={this.handleClick}>{name}</li>;
                })}</ul>);
        }
        }
        If the user clicks on the first name in the list exactly once, what number will be passed to addNumCallback? Briefly explain why
        """: "0 will be passed to addNumCallback. This is because setState is asynchronous; the new state is not available before addNumCallback is called.",
        "Describe how React Context helps solve the problems associated with passing props to deeply nested components. In your answer, mention one trade-off or consideration when using Context": "React Context allows values to be shared globally without prop drilling. A trade-off is that large or frequently changing context values can cause unnecessary re-renders.",
        "What is the purpose of the dependency array in the useEffect Hook?": "It controls when the effect runs and re-runs",
        "Briefly explain the difference between useState and useReducer": "useState manages simple local state; useReducer manages more complex state logic using a reducer and dispatch pattern",
        "Briefly describe what the render() method does and during what part(s) of the React Component Lifecycle would it be executed?": "The render method returns JSX and is executed during the mounting and updating phases",
        "Say I'm coding a React component and I update its state in the 'render' method. Explain what the outcome would be and why.": "It causes an infinite render loop because updating state triggers render again",
        r"""
        Convert this class component to a functional component using the useState hook. Explain the key differences:
        export default class NamesList extends React.Component {
        constructor(props) {
            super(props);
            this.state = {number: 0}
        }
        handleClick = () => {
            this.setState({number: this.state.number+1})
            this.props.addNumCallback(this.state.number);
        }
        render() {
            return (
                <ul>{this.props.names.map((name, index) => {
                    return <li key={index}
                        onClick={this.handleClick}>{name}</li>;
                })}</ul>);
        }
        }
        """: r"""
        function NamesList(props) {
            const [number, setNumber] = useState(0);

            const handleClick = () => {
                setNumber(number + 1);
                // Or better: setNumber(prev => prev + 1);
            };

            return (
                <div onClick={handleClick}>
                    Count: {number}
                </div>
            );
        }
        Key differences:

        1. State initialization
        a. Class: Requires constructor, super(props), and object syntax:
            this.state = { number: 0 }
        b. Hooks: Single line - const [number, setNumber] = useState(0)

        2. State updates
        a. Class: Must use this.setState({ number: ... }) and merge objects
        b. Hooks: Direct setter function: setNumber(1)

        3. Multiple state variables
        a. Class: All state in one object this.state = { ... }
        b. Hooks: Separate state variables:
            i.   const [number, setNumber] = useState(0);
            ii.  const [name, setName] = useState("");

        4. No `this` keyword

        5. Functional updates
        a. Class: this.setState(prevState => ({ number: prevState.number + 1 }))
        b. Hooks: setNumber(prev => prev + 1) ← cleaner for updates based on previous state
        """,
        """
        Explain the dependency array in useEffect. What happens with an empty array, no array, or specific dependencies?
        """: "No array runs after every render; empty array runs once; specific dependencies run when those values change",
        "Why is this wrong? if(user){ useEffect(() => {...});}": "Hooks cannot be called conditionally",
    },
    "InformationManagement": {
        "What term is used to describe program data that will survive exiting the application?": "Persistent",
        "Explain the difference between internal and external representations of program state (PS) data": "When An internal representation stores data in a form optimized for manipulation and system logic, such as Photoshop using layers and individual objects for editing and formatting. An external representation stores data in a form optimized for presentation or exchange, such as exporting the image as a flat array of pixels.",
        "What kind of access to I/O streams typically use?": "Sequential access",
        "What format are cookies stored in?": "Name value pairs",
    },
    "BackEndAPIs": {
        """What is the role of middleware in an Express.js back-end server? Provide a code example of a simple logging middleware and explain its execution flow.""": """
        Middleware in Express.js is a function that executes on every incoming request before reaching the final route handler. It can modify request/response objects, end the request-response cycle, or call the next middleware.
        app.use((req, res, next) => {
        console.log(`${req.method} ${req.url}`);
        next();
        });
        This logs the HTTP method and URL of each request and passes control to the next middleware or route handler
        """,
        "In the context of back-end servers, define an endpoint. Then, give two examples of device endpoints and give two examples of API URL endpoints.": """An endpoint is any remote computing entity or address that exchanges data over a network. 
            Device endpoints include a user's smartphone and laptop that send requests to the server. 
            API URL endpoints include routes like /movies or /users/:id that the server exposes. 
        """,
        """
        Explain which basic operation (e.g. create, read, etc) this represents and explain what the server does, line-by-line, when a client sends a PUT request with a JSON body to /movies/42.
        app.put("/movies/:id", async (req, res) => {
        const { id } = req.params;
        const newBody = req.body;
        const movie = await Movie.findByIdAndUpdate(id, newBody, { new: true });
        res.json(movie);
        });
        """:"""
        This route represents the Update operation in CRUD.
        Steps taken by server:
        The server extracts 42 as the ID and reads the new field values from req.body
        It calls Movie.findByIdAndUpdate("42", newBody, { new: true }) to modify the record in the database and get the updated version
        The updated movie document is then returned as JSON to the client
        """,
        "When an Express Router selects an endpoint for a request, which request attributes does it definitely consider?": "Request Method and Path",
        "What term did we use to describe what express.json() returns?": "middleware",
        "What term do we use to describe a number on which a server application can listen for requests and have the operating system forward such requests to it sent specifically to that number?": "Port",
        "In HW3, list the situations where you chose to use await.": "When calling a function using Mongoose; When sending a request using Axios",
        "In a JavaScript application, when should the await keyword be used, and why?": "await should be used when calling functions that return a Promise, where execution must pause until the asynchronous operation completes, such as database operations or network requests.",
        "The createNewList code snippet below is from HW 3 and is a programming trick to wrap an async function inside a synchronous one and was needed because inside asyncCreateNewList we wished to make use of what?": "await",
        "what is the Axios API?": "A facade for native request building",
        "List the main HTTP request methods used in a CRUD Web Application and briefly describe what each does": "GET retrieves data, POST creates data, PUT updates data, DELETE removes data",
        "What is an HTTP status code, provide examples and briefly describe what each means. (200, 201, 400, 404)": "200 success, 201 created, 400 bad request, 404 not found",
    },
    "FullStackWebApplications": {
        
        "In your Vitest script, you placed the mongoose.connect() call inside the beforeAll hook rather than beforeEach. What is the primary benefit of this approach for your test suite?": "It improves performances by establishing the expensive database connection only once for the entire file.",
        "You have written a test to verify that the retrieved user object matches your expectedUser object. Why would you likely use expect(actualUser).toEqual(expectedUser) instead of expect(actualUser).toBe(expectedUser)?": "Because toBe checks for reference equality (same memory location), while toEqual checks if the properties and values match (deep equality)",

        "In HWs 1-3, what technology was used to specify modal animations?": "CSS",
        "In JSX, what syntax do you use to embed a JavaScript expression inside markup?": "{ }",
        "In Postman, where do you set the raw JSON format for the request payload?": "Body",
        "What can you definitively say about a React component that is not currently mounted?": "It is not rendered; It may or may not be rendered (EITHER B OR C ACCEPTED)",
        "When implementing Drag and Drop in HWs 2 & 3, which callback function would we provide that would have to specify which song is actually being dragged by setting the card id in the event's dataTransfer object": "onDragStart",
        "When employing a grid layout using CSS for a container with 6 rows and 6 columns, if one wanted to put an element with an id of 'my-element' inside that container such that it covered two columns and three rows, what could we specify inside our style sheet": """
            my-element {
                grid-column: 3/5
                grid-row: 3/6
            }
            """,
        "How can we control what props are sent to downstream children in React?": "By specifying our own named property values for our component using JSX in the parent component's render function",
    },
    "DatabaseManagementSystems": {
        "How is data organized in a NoSQL database like MongoDB?":"Documents and collection",
        "In HW 2 our DBManager code saved data to where?": "Local Storage",
        "What Mongoose setting for your objects to be saved to MongoDB, if set to true, will record the date and time that a document is created, last accessed, and updated?": "timestamps",
        "Suppose a database contains two tables. Table A has 8 rows and Table B has 6 rows. If a JOIN is performed between these two tables without specifying any join condition, how many rows will appear in the result, and why?": "40",
        "In lecture we said that SQL falls into what language category?": "Declarative language",
        "When using Mongoose, _____________ defines the structure and blueprint of the data to be stored, specifying the fields and their types": "schema",
        "When using Mongoose, a ________________ is a constructor object that can be provided data for initializing a known database type which when invoked, returns an object capable of then being used for querying, updating, deleting, and saving data in the database.": "model",
        "What would we call an API that allows one to create, read, update, and delete things in a relational database in pure Javascript": "ORM",
        "In a MongoDB document, what is the purpose of the _id field?": "It serves as the primary key.",
        "In a mongodb doument, how is _id guaranteed to be unique?": "It will store 4 bytes for timestamp, 3 bytes for machine id, 2 bytes for process id, 3 bytes for incremental value.",
        """
        Given the following tables:
        Authors: author_id | name
        Books: book_id | title | author_id
        Write a query that lists each book title along with its author name, Fill in the missing part of the JOIN condition below.
        SELECT Books.title, Authors.name
        FROM Books
        JOIN Authors
        ON _______________;
        """: "ON Books.author_id = Authors.author_id",
        "When querying a MongoDB collection using a Mongoose model, name all of the parameters that can be used": "[id], [filter], [projection], [options], [update] and [conditions]",
        "What does the [id] parameter do": "applies some function to a specific document",
        "What does the [filter] parameter do": "The [filter] parameter combines conditions to provide a criteria of how a document is chosen",
        "What does the [condition] parameter do": "Gives a single conditional for how a document is chosen",
        "What does the [projection] parameter do": "The [projection] parameter specifies which fields from the selected documents should be returned",
        "What does the [options] parameter do": "Alters how the result is returned",
        "What does the [update] parameter do": "Specifies what changes to make to a document",
        r"""
        Based on the schema definition provided below, what specific data structure is expected for the songs field?
        const playlistSchema = new Schema({
        name: {type: String, required: true},
        songs: {type: [{
            title: String,
            artist: String,
            year: Number,
            youTubeId: String
        }], required: true}
        });
        """: "An array of objects, where each object must contain fields for title, artist, year, and youTubeId",
        "Write an SQL statement that changes Oscar Wilde's book title to 'The Picture of Dorian Gray.' where the table has columns 'BOOK_ID', 'TITLE', and 'AUTHOR_NAME'": "UPDATE Books SET TITLE = 'The Picture of Dorian Gray' WHERE BOOK_ID = 10569;",
        "Write one line of SQL code to retrieve all books written by Jane Austen when the table has columns 'BOOK_ID', 'TITLE', 'AUTHOR_NAME'": "SELECT * FROM Books WHERE AUTHOR_NAME = 'Jane Austen';",
        """
        Describe the relationship between Genres and books. Explain which column connects the two tables and what type of relationship it represents
        CREATE TABLE Genres (
        GENRE_ID int PRIMARY KEY,
        NAME varchar(100)
        );
        CREATE TABLE Books (
        ISBN char(13) PRIMARY KEY,
        TITLE varchar(100),
        AUTHOR_ID int,
        GENRE_ID int,
        FOREIGN KEY (GENRE_ID) REFERENCES Genres(GENRE_ID)
        );
        """: "The GENRE_ID column in the Books table connects each book to a genre in the Genres table. Each genre can include many books, but each book belongs to only one genre. This represents a one-to-many relationship from Genres to Books.",
    },
    "GeneralCourseInfrastructure": {
        "In npm, what does the 'p' stand for?": "package",
        "During our first lecture we said that doing great, _______ work is habit forming and doing mediocre, un_________ work is also habit forming": "focused",
        "What term did we say refers to a working class or API which may no longer be supported in future releases and so one is discouraged from using? If you recall, we said that Facebook has decidedly said React class-based Components will not be put into this category any time soon (but really who knows?).": "deprecated",
        "Currently, when using Git, what is the default branch for a repository named?": "main",
        "Currently, when using Git, what common name (which we used) is given to the remote repository?": "origin",
        "Because of the contents of our .gitignore file in HWs 1-3, what would be required of your Teaching Assistant in order to setup and test your work?": "Run the npm install command",
        "What does the command git clone https://github.com/TheMcKillaGorilla/316-HW1-Playlister . do and why does the period at the end matter?": "The command copies the remote repository into your current folder. The period tells Git to clone the files into this directory instead of creating a new subfolder, which can mess up relative paths",
        "What are some benefits of using version control systems like GitHub in software development?": "Version control systems enable collaboration and version history. Multiple developers can work together without overwriting each other's work and can easily track or revert changes when necessary",
    },
    "ComputerSecurityPrinciples": {
        "What is the difference between an app and a product?": "An app is something that runs; a product is something intentionally designed around users and quality.",
        "What is asset clarification": "Asset clarification is understanding what needs to be protected before deciding how to protect it.",
        "What is the most dangerous type of attack that developers must safeguard against and why": "Staff and programmers because may have a high level of access to sensitive systems",
        "What is OWASP": "the Open Web Application Security Project. They help give guides on how to protect software",
        "What are the 3 security reqirements": "Confidentiality, Integrity, and Availability",
        "What considerations are involved when designing a security system before its made?": """
        Threat models
        helps enumerate potential problems
        helps design & build secure systems
        Trust assumptions
        helps with abstraction layers
        Risk analysis
        spend time/money/resources properly
        """,
        "Name the security design principles": """
        Least Privilege
        Fail-Safe Defaults
        Economy of Mechanism
        Complete Mediation
        Open Design
        Separation of Privilege
        Least Common Mechanism
        Psychological Acceptability
        """,
        "What is the Least Privilege Security principle": "It is a security principle placed on abstraction layers that gives people the least amount of privlege they need.",
        "What is the Failsafe Default": "Programs default to not allowing access to things",
        "What is the Economy of mechanisms": "Principle that states security mechanisms should be as simple as possible",
        "What is the Complete mediation": "Always check access rights for every use",
        "What is the Open Design principle": "Security should not depend on the secrecy of the design",
        "What is the separation of privlege": "Allocate privlege based on the needs of users and processes",
        "What is the least common mechanism": "Minimize shared components or mechanisms between users or processes.",
        "What is psychological acceptability": "Don't make a product more difficult to use due to higher security",
        "What do firewalls do": "Monitors traffic and restricts access to addresses and ports",
        "What can JWTs be used for": "Storing accounts and login credentials",
        "What are the 8 principles of web security": """
        Authentication (confirm user identity)
        Authorization (specify access rights to resources)
        Confidentiality (message encryption)
        Data Integrity (data cannot be changed without detection)
        Message Integrity (messages cannot be changed without detection)
        Availability (no DNoS)
        Accountability (actions should be traceable)
        Non-repudiation (must be able to prove a transaction took place)
        """,
    },
    "FullStackWebSecurity": {
        """
        The following code snippet is taken from the back-end of a site that is stored passwords in a database. The first part is hashing and storing a password. The second part is verifying an entered passed. State what is wrong about the following lines of code.
        const saltRounds = 10;
        const salt = await bcrypt.genSalt(saltRounds);
        const passwordHash = await bcrypt.hash(password, salt);
        const newUser = new User({email, passwordHash});
        const savedUser = await newUser.save();
        … Some time later …
        const enteredPasswordHash = await bcrypt.hash(enteredPassword, salt); // Assume enteredPassword is a password entered by a user logging in
        const passwordCorrect = enteredPasswordHash === savedUser.passwordHash;
        """:
        """
        Comparing the passwords is done incorrectly as bcrypt hashing, even when using the same salts and hashing the same text, would result in different hashes. This means the login would always fail.
        The correct way to verify passwords would be: 
        const passwordCorrect = await bcypt.compare(enteredPassword, newUser.passwordHash);
        """,
        "Say a hacker sends hundreds of videos and photos to a server, overwhelming it to the point it cannot handle normal user requests. What kind of cyber attack is this?": "Denial of Service Attack (DOS)",
        "What's the primary reason why HTTPS is considered better than HTTP for transmitting sensitive data?": "its more secure due to it using SSL",
        "Describe the primary steps a server and client take during the user authentication strategy using a JSON Web Token (JWT), starting immediately after a user successfully logs in.": """
        The server makes and signs a JWT (token) using a server secret password and stores information like the user's ID inside it. 
        The server returns the JWT to the client, typically in an httpOnly cookie.
        For every subsequent request the user makes, the client's browser must send the JWT along with the request. 
        The server verifies the token using the site's secret. If the token is verified, the server trusts the user is who they claim to be and processes the request for a specified amount of time.
        """,

        "Name 3 certificate authorities": "Let's encrypt, Go Daddy, IdenTrust",
        "What do SSL certificates do?": "Verify the identity of a wbesite owner and enables encrypted communication between client and server",
        "How does SSL encrypt communication between client and server?": "Public/private key pairs",
        "How are authentication tokens stored and when are they made?": "They are made when users log in and stored as JSON Web Tokens (JWTs)",
        "What are 2 ways of storing your authentication token and which is better?": "httpOnly cookies > Local storage because local storage can be hacked with javascript",
        "Who signs your JWT": "The server using their secret password",
        "When is the token used by the client?": "Every time a request is sent to the server",
        "What are the parts of JWT": "Header, payload, signature",
        "Where is the server's secret password stored?": "in the signature of the JWT",
        "Where is algorithm of JWT stored": "In the header",
        "Where is the data of the JWT stored (the acutal data the client/server sends)": "the payload",
        "How are JWT urls encoded": """In Base-64 strings with each part separated by a dot
        e.g: XXX.YYY.ZZZ
        """,
        "Name the two main functions provided by Json Web Token in javascript?":"jwt.sign() and jwt.verify()",
        "What are the parameters for jwt.sign()":"A user id object and a JWT secret",
        "What are the parameters for jwt.verify()":"token and JWT secret",
        "Which end is responsible for providing user schemas, comparing passwords, and using middleware?": "backend",
        "Which end is responsible for sending register/login forms, filling out payload formats, and providing navigation routes": "frontend",
        "Which end is responsbile for password salting and providing controllers": "backend",
        """
        const mongoose = require('mongoose')
        const Schema = mongoose.Schema
        const UserSchema = new Schema(
          {
            email: { type: String, required: true },
            passwordHash: { type: String, required: true }
          },
          { timestamps: true },
        )

        __________________

        What line of code is required to actually export the schema?
        """:"module.exports = mongoose.model('User', UserSchema)",
        "What does salting a password do?":"Salting a password adds random data to the password before hashing so that identical passwords produce different hashes",
        "What are controllers responsible for in a full-stack web project":"They resolve requests made by backend rotues",
        """Name 5 of the 9 common techniques attackers use to attack a system?""":"""
        Birthday attack
        Cross-site scripting (XSS) attack
        Denial-of-service (DoS)/Distributed denial-of-service (DDoS) attacks
        Drive-by attack
        Eavesdropping attack
        Malware attack
        Man-in-the-middle (MitM) attack
        Password attack
        Phishing and spear phishing attacks
        """,
        "What do birthday attacks do":"Attackers attempt to produce the same hash as the user",
        "What does a cross-site scripting attack do":"Attackers use 3rd party resources to run script in the victim's browser using script injection",
        "What does a denial of service attack do?":"Overwhelm a system's resources so it cannot handle requests. Same thing as a DoS attack",
        "DoS vs DDoS?": "DoS is an attack from a single point, DDoS is distributed.",
        "Name 2 types of DoS attacks":"""
            TCP SYN flood attack
            Teardrop attack
            Smurf attack
            Ping of death attack
            Botnets (i.e. zombie systems)                
        """,
        "What do drive by attacks do?":"Find a weak site and plant malicious code like PHP. This site is then accessed by users later on",
        "What do eavesdropping attacks do?":"They intercept network traffic to read sensitive data. Packet sniffing and account hacking",
        "What is malware":"Unwanted software installed without your consent",
        "What is a man-in-the-middle attack?": "Attackers hijack a session between a client and server.",
        "What's a phishing attack?" : "A form of social attack where the malicious actor pretends to be a trusted source and asks you to do something to gain personal info or influence",
        "What's an attack that targets a specific party?" : "Spearphshing attack", 
        "What's a password attack?" : "Cracking passwords whether through packet sniffing, key loggers, learning about a user, etc.",
        "What are two countermeasures towards password attacks?" : "2FA, security questions, lock outs",
        "What is CORS": "Cross-origin Resource Sharing CORS allows a server to specify which external origins a browser is allowed to share responses with.",
        "Name 2 web security rules of thumb": """
            Do not store sensitive session data in Browser Storage
                i.e. Local Storage or Web Storage
            Do not store sensitive session data in Cookies
            Do not store plaintext passwords
            Do not transmit plaintext passwords
        """,
        "What algorithm does bcrypt use for hashing": "blowfish",
        "What is click jacking and how do we prevent it": "Click jacking is when an attacker attempts to make a user click on something unintended. We use helmets to prevent it.",
    },
    "ImportantPrinciplesOfCreatingASoftwareSolution": {
        "What are the important principles to apply when you want to create a good software solution?": "First Define the Problem. Design, then Code. Always Provide Feedback",
        "Name 5 properties of a high quality software system":
    """
        Correctness
        Efficiency
        Ease of use
        for the user
        for other programmers using your framework
        Reliability/robustness
        Reusability
        Extensibility
        Scalability
        Secure
    """,
    "What is correctness?": "Checks that the requirements are actually what the user wants, and that the code satisfies those requirements",
    "What is efficiency":"The choice of data structures and algorithms when designing software to meet performance expectations",
    "What is Ease of Use?":"A gui that prioritizes a gentle learning curve and familiar components",
    "What makes a framework easy to use?":"""
        logical structure (should mirror problem)
        naming choices (classes, methods, etc.)
        flexibility (usable for many purposes)
        feedback (exceptions for improper use)
        documentation (APIs & tutorials)
    """,
    "What is reliability/robustness": "Code that can antipicate user error and restrict choice to intended features",
    "What is graceful degradation?": "Code that knows what to do when things go wrong. Uncaught errors bad!!",
    "What kinds of feedback do you give to end users?":"Popup dialogs, highlights",
    "What kinds of feedback do you give to programmers?": "exception codes, error values",
    "What kinds of feedback are generated by users?": "Bad input, equipment failure, missing files",
    "What kinds of feedback are generated by programmers?": "Passing bad data, incorrect intialization",
    "Why should you give less feedback to an end user?": "it can be used by malicious actors to get unneeded information",
    "Why are making frameworks more difficult than applications":"Frameworks are harder because it must be flexible enough to work with many unknown applications",
    "What is reusability":"Code that serves multiple purposes",
    "How can we achieve reusability": "Separate technology dependent components. Decoupling is good!!",
    "What is extensibility": "A measure of how easily a software can be used for other purposes. Think plug-ins, extensions, add-ons, ect",
    "What is scalability":"How will a program perform as we increase the demand on resources",
    "What kinds of things can cause an increase of demand on product resources?": "# of user connections, increase of data being processed, and the range of geolocations requests are from",
    "Which properties is most directly supported by separating technology-dependent components from the rest of the system?": "Reusability",
    },
    "SoftwareDesign": {
        "What should be made when doing requirements analysis": "A Software Requirements Specification (SRS)",
        "What is an SRS?":"An SRS defines the problem we need to solve.",
        "What is the reccomended format of SRS?": """
            Explanation of problem
            Detailed description of Use Cases
            Mock-up diagrams of User Interface
            Summary
        """,
        "What is a UML Case Diagram?":"A Unified Modeling language that describes interactions between a user and system",
        "What are use case diagrams for and how are they formatted?": "They describe user secnarios and should start with verbs",
        "Name 5 of the 12 formal use case diagram fields":"""
        Use-Case Number
        Use-Case Name
        Actors
        Preconditions
        Postconditions
        Story
        Scenario
        Exceptions
        Priority
        When Available
        Frequency of use
        Open Issues
        """,
            "What are the steps of the software development lifecycle": """
        1.	Requirements analysis
        2.	Design & document
        3.	Design evaluation
        4.	Coding
        5.	Testing
        6.	Deployment
    """,
    "When should we consider applying properties of high quality software systems?":"During requirement analysis and design stage (early on!!)",
    "Whats the difference between an architect and a designer?": "Architects make big picture decisions. Designers create structural and functional code designs for modules architects create",
    "What was included in the Requirements Design of the final project?":"Use cases and User interface mockups",
    "What was included in the back-end api software design for the final project?": "Database Design, Endpoints, Security layer, Business logic, Queries",
    "What was included in the front-end software design for the final project?":"User interface components, data store managment, HTTP requests",
    "What accesses memory in Java and what else does it do?": "JVM/Java virtual machine is the runtime environment for Java code and is responsible for interacting with memory through addresses",
    "List the memory segments from highest value (0xffffff) to lowerst (0x000000)":"Stack, heap, Text, Global",
    "What data does the text field store?":"Program instructions",
    "What data do Global segments store?": "Data that can be reserved at compile time (static data)",
    "What does the Stack store?":"Stack stores temporary variables, method arguments, and is constantly added to and deleted",
    "What does the heap store?":"Heap stores dynamic data (every time you use new!!!), they store references and all objects are stored in heap.",
    "Which memory segment stores persistent data?": "heap",
    "Which memory segment stores function return values?": "stack",
    "What is the difference between apparent and actual type?": "Apparent type is what objects were DECLARED as, Actual types are what objects are CONSTRUCTED as",
    "Which type (apparent or actual) does the JVM use in runtime?": "Actual type",
    "Which type (apparent or actual) does the compiler use?": "Apparent",
    """
    class Animal {
        void speak() {
            System.out.println("Animal");
        }
    }

    class Dog extends Animal {
        void speak() {
            System.out.println("Dog");
        }
    }

    Animal a = new Dog();
    a.speak();


    What is the apaprent type of a? What is the actual type? What is printed?
    """: """Apparent type: Animal
            Actual type: Dog
            Printed output: Dog""",
    """
    class Vehicle {
        void move() {
            System.out.println("Vehicle");
        }
    }

    class Car extends Vehicle {
        void move() {
            System.out.println("Car");
        }
    }

    Vehicle v = new Car();
    Vehicle w = new Vehicle();

    v.move();
    w.move();
    
    what is the apparent and actual type of v and w? What is the output?
    """: 
    """
        v
        Apparent type: Vehicle
        Actual type: Car
        Output from v.move(): Car
        w
        Apparent type: Vehicle
        Actual type: Vehicle
        Output from w.move(): Vehicle
    """,
    """
    What is the relationship between Person and Student in the following code. Explain how you know.
    private class Person {
    protected String firstName;
    protected String lastName;
    ...
    public String toString()
    { return firstName + " " + lastName; }
    }
    private class Student extends Person {
    private double GPA;
    ...
    public String toString()
    { return "" + GPA; }
    }
    """ : "Student and Person has a IS-A relationship since Student extends Person",
    "Explain what an IS-A relationship is and how you can detect one": "IS-A relationships are superclass -> subclass relationships and all utilize the extend keyword",
    "Explain what a HAS-A relationship is and how you can detect one": "HAS-A relationships is an instance from another class created in the constructor, and do not utilize extend",
    """
    Explain the realtionship between engine and car. How do you know?

    private class Engine {
        private int horsepower;
        ...
        public int getHorsepower() {
            return horsepower;
        }
    }

    private class Car {
        private Engine engine;
        private String model;
        ...
        public String toString() {
            return model;
        }
    }
    """: "They have a HAS-A relationship because engine is created inside car. No extends keyword",
    """
    class Engine ()
    class Car {
        constructor() {
            this.engine = new Engine();
            }
    }

    Does this code represent Aggregation or Composition? Why?

    """: "Composition, because the Engine is created inside the Car's constructor and cannot exist independently of the Car instance.",
    "A car cannot exist without an engine. What kind of HAS-A relationship is it?":"Composition",
    "A car can exist without a dashcam. What kind of HAS-A relationship is it?": "Aggregation",
    "In UML, what denotes inheritance IS-A relationship between two diagrams?": "A solid line with open arrow pointing from CHILD -> PARENT",
    "In UML, what denotes interface IS-A relationships between two diagrams?":"A dotted line wit an open arrow pointing from CHILD -> INTERFACE",
    "In UML, what denotes HAS-A aggregation?":"Solid line with OPEN square. From the part to the whole",
    "In UML, what denotes HAS-A Composition?":"Solid line with CLOSED square. From part to the whole",
    "In UML, what denotes a use relationship? (variable, method, ect)":"Regular arrow towards class being used",
    """

    Fill in the UML diagram to represent a class Dog with:
	•	A private instance variable age : int
	•	A protected instance variable breed : String
	•	A public static variable species : String
	•	A public method bark() : void
	•	A private method calculateAgeInDogYears() : int

    +----------------------+
    |        Dog           |
    +----------------------+
    |                      |
    |                      |
    |                      |
    +----------------------+
    |                      |
    |                      |
    +----------------------+
    """: """
    +----------------------------------+
    |              Dog                 |
    +----------------------------------+
    | - age : int                      |
    | # breed : String                 |
    | + species : String {static}      |
    +----------------------------------+
    | + bark() : void                  |
    | - calculateAgeInDogYears() : int |
    +----------------------------------+
    """,

    """
    Fill in the UML diagram to represent an abstract class Vehicle with:
        •	One protected variable speed : int
        •	One public abstract method move() : void
        •	One public concrete method getSpeed() : int
        +------------------------------+
        |        Vehicle               |
        +------------------------------+
        |                              |
        +------------------------------+
        |                              |
        |                              |
        +------------------------------+
    """: """
    +--------------------------------+
    |        Vehicle {abstract}      |
    +--------------------------------+
    | # speed : int                  |
    +--------------------------------+
    | + move() : void {abstract}     |
    | + getSpeed() : int             |
    +--------------------------------+
    """,
    """
    Fill in the UML diagram to represent an interface Flyable with:
        •	One public static final variable MAX_ALTITUDE : int
        •	One public abstract method fly() : void
    
    +------------------------------+
    |                              |
    +------------------------------+
    |                              |
    +------------------------------+
    |                              |
    +------------------------------+

    """:
    """
    +--------------------------------+
    |          <<interface>>         |
    |            Flyable             |
    +--------------------------------+
    | + MAX_ALTITUDE : int {static}  |
    +--------------------------------+
    | + fly() : void {abstract}      |
    +--------------------------------+    
    """,
    },
    "GeneralizationAndSpecificationWithDatabases": {
    "What is GraphQL?": "Facebook Query Language ane execution engine where you specify what you want not how to get it",
    "Explain when findOne() should be used instead of find().": "findOne() returns the first element, find() returns an array of all elements",
    "Given Model.findById(req.params.id), what would happen if they can't find the document?": "Returns Null",
    "await Model.findById({ _id: req.params.id }); Why is this wrong? What is special about Mongoose methods that use the ID field?": "Mongoose methods that use ID requires id to be sent directly, it cannot be in an object",
    "A user opens a page that should display all published playlists created by a specific user. What query should be sent Mongoose?": "Playlist.find({ ownerEmail: userEmail })",
    "A user clicks on a playlist card, and the application needs to retrieve one playlist by its unique ID. What query should be sent to Mongoose?": "Playlist.findById(req.params.id)",
    "An admin deletes a playlist by clicking a delete button that sends the playlist's ID. What query should be sent to Mongoose?":"Playlist.findByIdAndDelete(req.params.id)",
    "The system needs to retrieve a single published playlist with the highest number of likes. What query should be sent to Mongoose?": "Playlist.findOne().sort({ likes: -1 })",
    "A user replaces all playlists owned by joe@shmo.com with a new playlist called newPlaylistObject. What query should be sent to Mongoose?": "Playlist.findOneAndReplace( { ownerEmail: req.params.ownerEmail }, newPlaylistObject )",
    """
    In software design, two or more classes share common attributes and behaviors. A developer extracts these shared characteristics into a single superclass so they can be managed in one place and reused by multiple subclasses.
    What software design concept is being applied, and what is its primary benefit?
    """: 
    """
    The software design concept being applied is software generalization.
    Its primary benefit is that shared attributes and behaviors can be managed in one place, reducing code duplication and improving reusability, flexibility, and maintainability.""",
    """
    A software system defines a general class that specifies common behavior through shared methods and interfaces. Individual subclasses then provide their own specific implementations to customize that behavior while still conforming to the general structure.
    What software design concept is being applied, and how is it typically achieved?
    """: """
    The software design concept being applied is software specialization.
    It allows generalized types to be customized by subclasses that provide specific implementations, increasing flexibility while preserving a common structure.""",
    "How did we generalize CRUD on our playlister?": "We used a Database manager. ODM for MongoDB and ORM for MySQL",
    "":"",
    },
    "DesignReview": {
        "Describe the critical design issues": "Is it correct? Is it efficient? Is it testable & maintainable? Is it modifiable/extensible/scalable?",
        "What perspectives make a good design commitee":"both internal and external to project",
        "What is modular design": "Design that is split into separate modules",
        "Explain the workflow when designing a modular design": "Decompose: Divide into sub problems. Solve: Solve each part independently. Assemble: combine modules to make a full system",
        "What are traits of good modular design?":"Explicit and minimized connections between modules, Independent implementaiton, and good abstraction",
        "What is the narrow interface principle?":"Modules should only have access to as much information as it needs to work.",
        "What local properties do we need to ensure?": "Consistency, completeness, performance",
        "What proven and systematic procedure should you use when reviewing design instead of testing and verifying? " :  "Examining both the local and global properties of the design ",
        "When reviewing a software design for correctness, what are local properties? " :  "Local properties are characteristics evaluated at the level of individual modules. ",
        "Explain what global properties are in design review. ":  "Global properties concern how modules interact and fit together after local properties are verified. ", 
        "Describe the main global aspects that should be considered ":  """
        1. All data from the original SRS is accounted for
        2. Tracing paths through the design using walkthroughs and selected test data to verify that both data and control flows correctly through the design. """,
        "What key questions should you be asking to evaluate modularization? ":  "Is there an abstractino for better modularization? Have we grouped things that don't belong in the same module?",
        "What are main structural considerations when assessing design structures?": "Coherence of procedures, coherence of types, communication between modules, reducing dependencies",
        "What's Coherence of Procedures?": "Procedures within a module belong together",
        "What indicates lack of coherence of procedures?": "The best way to specify a procedure is to describe how it works because it's difficult to name it",
        "What's Coherence of Types?": "Data types in the same module are closely related and represent a single, consistent concept.",
        "What's Communication between Modules?": "Interactions between modules are clear and well-defined.",
        "What is a good way to expose design flaws?": "Attempt to break the program by exploiting edge cases",
        "Why is software design with fewer dependencies generally preferred?": "Because each component dependent on as few other components as necessary so it's easy to modify and test.",
        "What are antipatterns?": "They are common patterns in programs that use poor design concepts, such as spaghetti code and the blob.",
        "What design anti-pattern am I describing and what are its consequencies? : Single class with many attributes & operations, controller class with simple, data-object classes.": "It's The Blob. The consequencies are code being too complex to reuse or text and being expensive to load.",
        "What's sphaghetti code?": "An undocumented piece of software source code that cannot be extended or modified without extremem difficulty due to its convoluted structure.",
        "What are design principles?": "A basic tool or technique that can be applied to designing or writing code to make that code more maintainable, flexible, or extensible.",
        "What are the 5 design principles?": "Cohesion, Open-Closed Principle, Don't Repeat Yourself Principle, Single Responsibility Principle, Liskov Subsitition Principle",
        "What does a cohesive class do?":"It does one thing really well and does not try to do or be something else.",
        "What is the Open-Closed Principle or OCP?": "It says that classes should be open for extension but closed for modification. As in it should allow for change but not by modifying the original code.",
        "What is the Don't Repeat Yourself Principle or DRY?": "It states to avoid duplicate code and have each piece of information and behavior in a single, sensible place.",
        "What is the Single Responsibility Principle or SRP?": "Every object should have a single responsibility and all the object's services should be focused on carrying out that responsibility.",
        "What is the Liskov Substition Principle or LSP?": "All subtypes must be substitutable for their base types.",
        },
    "OutputQuestions": {
        """

        function Counter() {
        const [count, setCount] = React.useState(0);

        function handleClick() {
            setCount(count + 1);
            setCount(count + 1);
        }

        return <button onClick={handleClick}>{count}</button>;
        }

        After one click, what is displayed?
        """: "1",

        """
        function Counter() {
        const [count, setCount] = React.useState(0);

        function handleClick() {
            setCount(c => c + 1);
            setCount(c => c + 1);
        }

        return <button onClick={handleClick}>{count}</button>;
        }

        After one click, what is displayed?
        """: "2",



        """

        function areas51(shapes: IShape[]) {
            let width = 51;
            for (let i = 0; i < shapes.length; i++) {
                let shape: IShape = shapes[i];
                console.log(shape.getArea(width));
            }
        }
        let shapes: IShape[] = [];
        shapes.push(ShapeFactory.createCircle());
        shapes.push(ShapeFactory.createSquare());
        areas51(shapes);
        When this code runs, two different area values are printed.
        Explain why the output differs for each element in the array, even though both elements are typed as IShape.

        """: "Even though both values are typed as IShape, the factory creates objects of different actual types (Circle and Square). When getArea() is called, each object uses its own underlying implementation.",
        """
        Consider the following backend code snippet using Mongoose:
        await Top5List.findById(
            { _id: req.params.id },
            (err, list) => {
                if (err) console.log("Not found");
                else console.log("Retrieved:", list.name);
            }
        );
        What will be printed to the console if the ID exists in the database and retrieval succeeds?
        """: "'Retrieved:' followed by the value of list.name",
        "In the context of Mongoose functions for finding and modifying data, what is the core functional difference between Model.findOneAndRemove() and Model.findByIdAndRemove()?": "findOneAndRemove can search for any field, where findByIdAndRemove can only search by ID",
        "":"",
       r"""
        Given the following code, what will be logged and why?
        function Animal(){}
        Animal.prototype.speak=function(){return \"sound\";};
        function Dog(){}
        Dog.prototype=Object.create(Animal.prototype);
        Dog.prototype.constructor=Dog;

        const myDog=new Dog();

        console.log(myDog instanceof Dog);
        console.log(myDog instanceof Animal);
        console.log(myDog.speak());
        """: "true, true, sound",

        """
        function test() {
            if (true) {
                var x = 10;
                let y = 20;
            }
            console.log(x);
            console.log(y);
        }
        test();
        """: """10
                undefined""",
        """
        const user = { name: "Alice" };
        user.name = "Bob";
        console.log(user.name);

        user = { name: "Charlie" };
        console.log(user.name);

        What would the output be?
        """: 
        """
        Bob
        TypeError
        """,
        """
        console.log(0 == false);
        console.log(0 != false);
        console.log(0 === false);
        console.log(0 !== false);
        What is the output? Explain why
        """:"""
        true
        false
        false
        true
        """,
        """
        function Point(x, y) {
            this.x = x;
            this.y = y;
        }

        let p = new Point(4, 5);

        p.z = 10;

        let action = "clear";

        p[action] = function () {
            this.x = 0;
            this.y = 0;
            this.z = -1;
        };

        p.clear();

        console.log(p.x, p.y, p.z);        
        """: "0 0 -1",
        """
        function multiplyByTwo(x) {
            console.log(x * 2);
        }

        function processNumber(callback) {
            let value = 7;
            callback(value);
        }

        processNumber(multiplyByTwo);
        What is the output of this question?
        """: "14",
    },
    "CreationalDesignPatterns":{
        "What is a design pattern?": "A description of a problem and its solution that you can apply to many similar situations",
        "Why are design patterns important?" : "It facilitates resuse of good, well-tested solutions and capture the structure and interaction between components.",
        "What are the 5 creational design patterns?" : "Builder, Factory method, Abstract factory, Prototype, Singleton",
        "Suppose you are implementing a graphics device object that will need to talk to your GPU and its instantiation and initialization has complex dependencies on other types. What design pattern should you use?": "Builder",
        "When should you use Builder design pattern?" : "When you want to encapsulate the construction of a complex object and allow it to be constructed in steps while hiding the internal representation from the client.",
        "What is a trait that the best builders share?" : "They are Data-Driven",
        "When should you use Factory design pattern?": "When multiple related concrete types share a common interface or superclass, and when client code should depend only on the apparent type rather than specific implementations",
        "When should you use the Abstract Factory design pattern?": "When you want to make a factory that creates factories",
        "When should you use the prototype pattern?":"When creating an instance of a given class is either expensive or complicated",
        "What is a drawback to prototype?": "A drawback to using the Prototype is that making a copy of an object can sometimes be complicated.",
        "When pick Singleton?": "When you only need one instance of a class and the instance needs to be shared",
        "What design pattern is employed for the implementation of Javascript objects?": "prototype",
        "Singleton drawback?": "Global state makes it hard to test",
        "What design pattern is employed for the implementation of Javascript objects?": "Prototype",

    },
    "StructuralDesignPatterns": {
        """Which design pattern is demonstrated when a React component wraps another component to add styling or functionality without modifying the original component? What principle does this follow?
        """: "Decorator",
        "When should the Adapter design pattern be used?":"Use the Adapter pattern when you need to integrate a new or third-party component with an incompatible interface into an existing system without modifying the existing code.",
        "CSS library might employ what design pattern when defining a FancyDiv? function FancyDiv() { return <div style = 'background-color:pink; color:white'/> }":"Decorator",
        "What design pattern did we employ when implementing our DatabaseManager in HW4?": "Bridge or Strategy",
        """
        You are developing a graphics application that supports different shapes (such as circles and rectangles) and must render them using multiple rendering engines (for example, OpenGL, DirectX, or a software renderer). You want to be able to add new shapes or new rendering engines without modifying existing shape or renderer code.
        Which design pattern should be used to solve this problem?
        """: "Brdige design pattern",
        "When do we choose the bridge design pattern?":"When you need to separate an abstraction from its implementation so you can change them independently",
        "When should the decorator pattern be used?": "When you want classes to be easily extended to add new behavior without modifying code",
        "When do you pick the facade pattern?":"When you want to simplify functionality by restricting choice",
        "Axios is an example of which design pattern?": "facade",
        "When do you want to use the flyweight pattern":"When an immutable, expensive object needs to be represented by multiple instances",
        "What is the most famous example of the flyweight pattern": "Strings",
        "When do you want to use the proxy pattern": "Use the Proxy pattern when you need a stand-in object that controls access to a real object."
    },
    "BehavioralDesignPatterns": {
        "Express middleware uses which design pattern?":"Chain of Responsibility",
        "When should you choose the Chain of Responsibility design pattern?": "When you want a request to be optionally handled by many different handlers",
        "When do you pick interpreter?":"when you need to define a grammar for a simple language and repeatedly evaluate or interpret expressions written in that language",
        "When do you choose an iterator?":"When you need to visit every element of a collection once.",
        "What are famous examples of iterator": "Java's for loops. Hashmaps. ArrayLists",
        "When do you use mediator?": "When many objects need to communicate and you want to reduce coupling by routing all interaction through a central mediator instead of direct object-to-object communication",
        "What are two examples of the mediator pattern?":"Express routers and GUI event dispatchers",
        "What are the 3 parts of the Momento and what are they for?":"Originator. Make some object with internal state. Caretaker - Make use of the originator and might restore state. The Momento - A read-only store of the previous state of the originator",
        "What is an example of the Momento pattern?": "jsTPS, aka our undo function in playlister",
        "When do you pick the observer design pattern?":"When you need an object's state to notify other objects, while remaining decoupled",
        "how does the observer pattern avoid tightly coupled components":"It makes observers depend on a common interface for updates, not on each other. It also allows a one-to-many relationship",
        "What design pattern does MVC use?":"Observer pattern",
        "What design pattern does React use?": "Observer pattern",
        "React uses the Flux design pattern, which is really their own flavor of what common design pattern?": "Observer pattern",
        "When do we use the state pattern?":"When behavior needs to change at runtime based on internal state WITHOUT too much conditional logic",
        "What pattern does Java I/O compression use?":"Strategy pattern",
        "What pattern does Java's Collections.sort() use?": "Strategy pattern",
        "When do you use strategy?": "When you have multiple algorithms or behavior you need to run at runtime, and they are INTERCHANGABLE",
        "Strategy pattern is commonly referred to as": "Algorithm in a box",
        "What design pattern lets one hook into an algorithm by overriding hook functions?": "Template pattern",
        "What uses Template pattern?": "Framework lifecycle methods, and Java I/O streams",
        "When do you want to use template?": "When you have a fixed algorithm structure but you want to delegate specific steps to a subclass.",
        "Which pattern is referred to as 'double dispatch'? What does double dispatch mean?": "Visitor pattern, and its another word for multiple polymorphism",
        "When do you select the visitor pattern?":"When you need to perform many different operations on a fixed set of object types without modifying their classes, and you want to keep those operations separate from the object structure. ",
        "What is component architecture?": "When a class/system is made up of swappable components.",
        "What famously uses component architecture": "Web browsers and react",
        "Implementing a class using the component architecture design pattern is usually done to avoid rigid class scaffolding. What is class scaffolding and why might rigid class scaffolding be bad?": """
        Rigid class scaffolding is when structure is determined by a large inheritance hierchy, where all behavior is determined by parent classes.
        Its bad because it makes structures highly coupled and reduces flexibility.""",
        """        
        function areas51(shapes: IShape[]) {
        let width = 51;
        for (let i = 0; i < shapes.length; i++) {
            let shape: IShape = shapes[i];
            console.log(shape.getArea(width));
        }
        }
        let shapes: IShape[] = [];
        shapes.push(ShapeFactory.createCircle());
        shapes.push(ShapeFactory.createSquare());
        areas51(shapes);
        When this code runs, two different area values are printed.
        Explain why the output differs for each element in the array, even though both elements are typed as IShape.
        Also note which design pattern is responsible for this?
        """: "The apparent type for both are IShape, but the actual type is different (circle and square). This is an example of the Strategy design pattern",
        """
        In Super Mario World, Koopas appear repeatedly in different positions, but they all share the same artwork and attributes. Suppose your game stores one fully configured Koopa, including its model and behavior, and wants to generate new Koopas with different positions but otherwise identical configuration.
        What design pattern should be used to create each new Koopa, and why is this approach preferable to building each Koopa from scratch?
        """: "Prototype design pattern",
        """
        What is the key difference between the Strategy pattern and the Template Method pattern in terms of how they achieve algorithm flexibility?
        """: "Strategy uses composition (HAS-A) to delegate to interchangeable algorithm objects at runtime. Template Method uses inheritance (IS-A) where subclasses override specific steps of an algorithm defined in a base class.",

    }
}