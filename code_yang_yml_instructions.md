# Chapter 3: YANG and XML

## Task 3.1: module, namespace, prefix, container, leaf, and leaf-list statements

### **Objective:** Write your own data model and payload

Create a basic YANG model that matches the following **pyang** output:

```sh
$ pyang ccdeve-candidate-module.yang -f tree
module: ccdeve-candidate-module
  +--rw candidate
     +--rw name?            string
     +--rw age?             int8
     +--rw certification*   string   <- Ensure multiple certifications are supported
```

Write an XML payload file that matches the YANG model, and validate it with `yang2dsdl`:

```sh
$ yang2dsdl -v ccdeve-candidate-data.xml ccdeve-candidate-module.yang
```

You can use the following code snippet as a starting point for the XML file:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <candidate xmlns="http://devnetexperttraining.com/...">
        <element1>data1</element1>
        <element2>data2</element2>
    </candidate>
</data>
```

### **Hints:**
- YANG RFC 6020 documentation: [YANG RFC 6020](https://www.rfc-editor.org/rfc/rfc6020.html)
- Docs → **4.2.2.5 Example Module**
- Docs → **7.1 The module Statement**
- Docs → **7.6 The leaf Statement**
- Docs → **7.7 The leaf-list Statement**
- Use the following command to view the documentation for **pyang tree** output symbols:

```sh
pyang --tree-help
```

## Task 3.2: list, grouping, key, leafref

### **Objective:** Create a scalable and resilient data model that represents a network topology consisting of devices and links

Create a YANG model that matches the `pyang` output below, as well as the following requirements:

- The common schema for the “a” and “b” side of each link must only be defined once by using a grouping statement
- `cable_length` must allow two decimal digits in the value. Examples: `1.00`, `22.11`, `30000.10`
- This model describes a network topology including a number of devices and the physical links between them. Every link has an “a”-side and a “b”-side and represents a physical cable with two ends.

```sh
$ pyang ccdeve-topology-module.yang -f tree
module: ccdeve-topology-module
  +--rw topology
     +--rw device* [name]
     |  +--rw name    string
     |  +--rw sku?    string
     +--rw link* [name]
        +--rw name     string
        +--rw a
        |  +--rw device      -> ../../../device/name
        |  +--rw ip_address? string
        |  +--rw interface   string
        +--rw b
        |  +--rw device      -> ../../../device/name
        |  +--rw ip_address? string
        |  +--rw interface   string
        +--rw cable_length?  decimal64
```

Write an XML payload file that matches the YANG model, and validate it with `yang2dsdl`:

```sh
$ yang2dsdl -v ccdeve-topology-data.xml ccdeve-topology-module.yang
```

### **Hints:**
- YANG RFC 6020 documentation: [YANG RFC 6020](https://www.rfc-editor.org/rfc/rfc6020.html)
- Docs → **7.8 The list Statement**
- Docs → **7.11 The grouping Statement**
- Docs → **7.12 The uses Statement**
- Docs → **9.9 The leafref Built-In Type**
- To remove the `pyang` node question mark and make a YANG leaf required, use:
  ```yang
  mandatory true;
  ```

## Task 3.3: pattern, length, range, and import statements

### **Objective:** Restrict inputs to conform with predefined format in a model that represents a single network device

Copy the file `~/venvs/main/share/yang/modules/ietf/ietf-inet-types.yang` to your working directory. You will be using this file to import an existing type definition into your own model.

Create a YANG model that matches the `pyang` output below, as well as the following requirements:

- Device hostname length must be between 1 and 20 characters
- VRF names should be restricted to the characters **A-Z**
- Valid loopback interface number is in the range **0-2147483647**
- Valid VLAN IDs are in the range **2-1001 and 1006-4094**
- VLAN name length must be between **1 and 32 characters**

```sh
$ pyang ccdeve-device-module.yang -f tree
module: ccdeve-device-module
  +--rw device
     +--rw hostname?           string
     +--rw vrfs*               string
     +--rw primary-loopback
     |  +--rw number?          uint32
     |  +--rw ip-address?      inet:ipv4-address
     |  +--rw prefix-length?   uint8
     +--rw vlans* [id]
        +--rw id               uint16
        +--rw name?            string
```

Write an XML payload file that matches the YANG model, and validate it with `yang2dsdl`:

```sh
$ yang2dsdl -v ccdeve-device-data.xml ccdeve-device-module.yang
```

## **Task 3.4: Score Report XML for Pass and Fail**

### **✅ Passed Score Report XML**
```xml
<score-report>
    <candidate-name>Sushil Bhattacharjee</candidate-name>
    <status>PASSED</status>
    <devnet-number>CSCO14529501</devnet-number>
</score-report>
```

### **❌ Failed Score Report XML**
```xml
<score-report>
    <candidate-name>Sushil Bhattacharjee</candidate-name>
    <status>FAILED</status>
    <software-design>57%</software-design>
    <infrastructure-as-code>72%</infrastructure-as-code>
    <automation>68%</automation>
    <containers>70%</containers>
    <security>88%</security>
</score-report>
```

Now, validate these XML files using:
```sh
$ yang2dsdl -v ccdeve-score-report-passed.xml ccdeve-score-report.yang
$ yang2dsdl -v ccdeve-score-report-failed.xml ccdeve-score-report.yang
```

